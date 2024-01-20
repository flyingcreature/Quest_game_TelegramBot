import telebot
from telebot import apihelper
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton
from info import location_data
import json
from dotenv import load_dotenv
from os import getenv

load_dotenv()
token = getenv("BOT_TOKEN")

bot = telebot.TeleBot(token)


def load_data() -> dict:
    """Функция загрузки данных из json."""
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {}


def save_data(data: dict):
    """Функция сохранения данных в json."""
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


user_data = load_data()


def create_markup(answers: list):
    """Функция сборки клавиатуры."""
    markup = ReplyKeyboardMarkup()

    for answer in answers:
        markup.add(answer)

    return markup


@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    """Функция обработки команды /start."""
    markup = ReplyKeyboardMarkup()

    user_id = message.from_user.id

    if str(user_id) not in user_data:
        markup.add(KeyboardButton("Начать приключение"))

        text = f"Привет, {message.from_user.username}. Скорее пройди этот квест!"

        user_data[str(user_id)] = {
            "Имя": message.from_user.username,
            "location": "start",
            "scale": 0,
        }
        save_data(user_data)

    elif str(user_id) in user_data and user_data[str(user_id)]["location"] != "start":
        markup.add(KeyboardButton("Продолжить"), KeyboardButton("Начать заново"))

        text = f"С возвращением, {message.from_user.username}! Хочешь продолжить прохождение квеста?"

    else:
        markup.add(KeyboardButton("Начать приключение"))

        text = f"С возвращением, {message.from_user.username}! Скорее пройди эту викторину."

    bot.send_message(
        chat_id=user_id,
        text=text.format(message.from_user.username),
        reply_markup=markup,
    )


def filter_continues(message: Message):
    """Функция-фильтр, для продолжения квеста с текущим показателем location пользователя."""
    keywords = ["Продолжить", "Начать приключение"]
    return message.text in keywords


@bot.message_handler(func=filter_continues)
def continue_solution(message: Message):
    """Обработчик продолжения квеста."""
    user_id = message.from_user.id
    go_to_location(user_id)


def filter_restart(message: Message):
    """Функция-фильтр, для рестарта викторины с обнуленным показателем progress пользователя."""
    return "Начать заново" == message.text


@bot.message_handler(func=filter_restart)
def restart_solution(message: Message):
    """Обработчик рестарта квеста."""
    user_id = message.from_user.id
    user_data[str(user_id)]["location"] = "start"
    user_data[str(user_id)]["scale"] = 0
    save_data(user_data)

    go_to_location(user_id)


def go_to_location(user_id):
    """Функция отправки вопроса."""
    location = user_data[str(user_id)]["location"]
    text, dop_mes, choices, scale, image_path = location_data[location].values()
    markup = create_markup(choices)
    # bot.send_photo(
    #     chat_id=user_id,
    #     photo=open(image_path, "rb")
    # )

    bot.send_message(
        chat_id=user_id,
        text=text,
        reply_markup=markup
    )
    bot.send_message(
        chat_id=user_id,
        text=dop_mes,
        reply_markup=markup
    )


def end_game(user_id):
    location = user_data[str(user_id)]["location"]
    text = location_data[location]["message"]

    markup = ReplyKeyboardMarkup()
    markup.add("Начать заново")

    user_data[str(user_id)]["location"] = "start"
    user_data[str(user_id)]["scale"] = 0
    save_data(user_data)
    bot.send_message(
        chat_id=user_id,
        text=text,
        reply_markup=markup
    )


def ending(user_id):
    if user_data[str(user_id)]["scale"] < 19:
        text = location_data["Плохая концовка"]["message"]
    else:
        text = location_data["Хорошая концовка"]["message"]

    markup = ReplyKeyboardMarkup()
    markup.add("Начать заново")

    bot.send_message(
        chat_id=user_id,
        text=text,
        reply_markup=markup
    )

    end_game(user_id)


@bot.message_handler(func=lambda message: True)
def handle_answer(message):
    """Обработчик ответов пользователя."""
    user_id = message.chat.id

    if str(user_id) not in user_data:
        return send_welcome(message)

    location = user_data[str(user_id)]["location"]
    choices = location_data[location]["choices"]
    user_choice = message.text

    if user_choice not in choices:
        bot.send_message(
            user_id, "Пожалуйста, выберите один из предложенных вариантов."
        )
        return

    user_data[str(user_id)]["location"] = user_choice
    scale = location_data[user_choice]["scale"]
    user_data[str(user_id)]["scale"] += scale
    save_data(user_data)
    try:
        if user_data[str(user_id)]["location"] not in ["Узнать результаты"]:
            if scale != 0:
                go_to_location(user_id)
            else:
                end_game(user_id)
        else:
            ending(user_id)
    except apihelper.ApiTelegramException:
        pass


bot.polling(none_stop=True)
