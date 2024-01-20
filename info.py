location_data = {
    "start": {
        "message": "В результате ядерного взрыва тебя откидывает в прошлое"
                   " и вы меняетесь телами с Кириллом Казаковым."
                   " Теперь, чтобы выжить, тебе нужно прожить 1 его день.",
        "dop_mes": "Вопрос 1: Ты просыпаешься в кровати . Что будешь делать дальше?",
        "choices": ["Пойти в колледж", "Пойти по прогать", "Поиграть в PlayStation5", "Лечь спать дальше"],
        "scale": None,
        "image": "start.jpg",
    },
    "Пойти в колледж": {
        "message": "Ты сделал правильный выбор, что пошел на пары.",
        "dop_mes": "Вопрос 2: После пар ты сильно устал. Что будешь делать дальше?",
        "choices": ["Поехать помогать родственникам", "Пойти на тренировку", "Вернуться домой и отдохнуть",
                    "Пойти гулять с друзьями"],
        "scale": 5,
        "image": "loc_1.jpg",
    },
    "Пойти по прогать": {
        "message": "Ты не уследил за временем"
                   " и не успел на первые 2 пары но ты успеваешь на следующие!",
        "dop_mes": None,
        "choices": ["Пойти на пары", "Продолжить заниматься своими делами"],
        "scale": 2,
        "image": "loc_2.jpg"
    },
    "Поиграть в PlayStation5": {
        "message": "Ты не уследил за временем"
                   " и не успел на первые 2 пары но ты успеваешь на следующие!",
        "dop_mes": None,
        "choices": ["Пойти на пары", "Продолжить заниматься своими делами"],
        "scale": 2,
        "image": "loc_2.jpg"
    },
    "Лечь спать дальше": {
        "message": "К сожалению ты очень увлёкся и не заметил, как прошел день."
                   "Когда решил посмотреть на время, увидел, что уже 21:00,"
                   " случился ядерный взрыв и ты погиб. Начни сначала.",
        "dop_mes": None,
        "choices": ["Lose"],
        "scale": 0,
        "image": "loc_3"
    },
    "Пойти на пары": {
        "message": "Ты сделал правильный выбор, что пошел на пары",
        "dop_mes": "Вопрос 2: После пар ты сильно устал. Что будешь делать дальше?",
        "choices": ["Поехать помогать родственникам", "Пойти на тренировку", "Вернуться домой и отдохнуть",
                    "Пойти гулять с друзьями"],
        "scale": 1,
        "image": "Loc"
    },

    "Продолжить заниматься своими делами": {
        "message": "К сожалению ты очень увлёкся и не заметил, как прошел день."
                   "Когда решил посмотреть на время, увидел, что уже 21:00,"
                   " случился ядерный взрыв и ты погиб. Начни сначала.",
        "dop_mes": None,
        "choices": ["Lose"],
        "scale": 0,
        "image": "Loc"
    },
    "Поехать помогать родственникам": {
        "message": "Ты поехал в деревню помогать родственникам с постройкой дома."
                   " Это заняло очень много времени и ты не успел к 21:00 добраться до дома."
                   " Случился ядерный взрыв и ты погиб. Начни день сначала.",
        "dop_mes": None,
        "choices": ["Lose"],
        "scale": 0,
        "image": "loc_1_1.jpg",
    },
    "Пойти на тренировку": {
        "message": "Ты сделал правильный выбор, что пошел на тренировку",
        "dop_mes": "Вопрос 3: Ты приехал на тренировку , прошёл турникеты и встретил тренера."
                   " Он дал план тренировки, ты посчитал его слишком сложным. Что будешь делать?",
        "choices": ["Выполнить тренировку с трудом, но полностью", "Сделать, что сможешь", "Забить на задание",
                    "Пойти к другому тренеру"],
        "scale": 5,
        "image": "loc_1_2.jpg",
    },
    "Вернуться домой и отдохнуть": {
        "message": "У тебя не получилось отдохнуть, потому что заела совесть, что будешь делать?",
        "dop_mes": None,
        "choices": ["Всё же пойти на тренировку", "Позвонить тренеру, и предупредить об отмене"],
        "scale": 2,
        "image": "loc_1_2_1.jpg",
    },
    "Пойти гулять с друзьями": {
        "message": "Все твои друзья заняты своими делами, поэтому тебе не удалось погулять."
                   " Выбери, что будешь делать дальше",
        "dop_mes": None,
        "choices": ["Всё же пойти на тренировку", "Позвонить тренеру, и предупредить об отмене"],
        "scale": 2,
        "image": "loc_1_2_2.jpg"
    },
    "Всё же пойти на тренировку": {
        "message": "Ты сделал правильный выбор, что пошел на тренировку",
        "dop_mes": "Вопрос 3: Ты приехал на тренировку , прошёл турникеты и встретил тренера."
                   " Он дал план тренировки, ты посчитал его слишком сложным. Что будешь делать?",
        "choices": ["Выполнить тренировку с трудом, но полностью", "Сделать, что сможешь", "Забить на задание",
                    "Пойти к другому тренеру"],
        "scale": 1,
        "image": "loc_1_2_2.jpg"
    },
    "Позвонить тренеру, и предупредить об отмене": {
        "message": "Ты не пошел качат пресс, бегат и отжумания. Провел свой день не по канону."
                   " Не заметил, как пролетело время. В 21:00 случился ядерный взрыв и ты погиб. Начни сначала",
        "dop_mes": None,
        "choices": ["Lose"],
        "scale": 0,
        "image": "loc_1_2_2.jpg"
    },
    "Выполнить тренировку с трудом, но полностью": {
        "message": "Ты сделал правильный выбор."
                   "Тренировка закончена, пора ехать домой",
        "dop_mes": "Вопрос 4: На чем решишь поехать домой?",
        "choices": ["На своей машине", "На автобусе", "На такси"],
        "scale": 5,
        "image": "loc"
    },
    "Сделать, что сможешь": {
        "message": "Силы на исходе, что будешь делать?",
        "dop_mes": None,
        "choices": ["Завершить тренировку", "Попытаться осилить тяжелые задания"],
        "scale": 2,
        "image": "loc"
    },
    "Забить на задание": {
        "message": "Тренер разозлился на тебя и выгнал навсегда с тренировок."
                   " Теперь ты не можешь вернуться домой и рассказать о случившимся родителям."
                   " Из-за этого ты не являешься домой в 21:00, взрывается бомба, и ты погибаешь. Начни сначала",
        "dop_mes": None,
        "choices": ["Lose"],
        "scale": 0,
        "image": "loc"
    },
    "Пойти к другому тренеру": {
        "message": "Тренер разозлился на тебя и выгнал навсегда с тренировок."
                   " Теперь ты не можешь вернуться домой и рассказать о случившимся родителям."
                   " Из-за этого ты не являешься домой в 21:00, взрывается бомба, и ты погибаешь. Начни сначала",
        "dop_mes": None,
        "choices": ["Lose"],
        "scale": 0,
        "image": "loc"
    },
    "Завершить тренировку": {
        "message": "Тренер разозлился на тебя, потому что ты рано завершил тренировку."
                   " Тебе стало грустно от этого, ты сел на трибуну и смотрел, как занимаются остальные."
                   " Ты не заметил, как время уже 21:00, а ты не дома."
                   "Произошел взрыв бомбы, ты погибаешь Начни сначала.",
        "dop_mes": None,
        "choices": ["Lose"],
        "scale": 0,
        "image": "loc"
    },
    "Попытаться осилить тяжелые задания": {
        "message": "Ты сделал правильный выбор."
                   "Тренировка закончена, пора ехать домой",
        "dop_mes": "Вопрос 4: На чем решишь поехать домой?",
        "choices": ["На своей машине", "На автобусе", "На такси"],
        "scale": 1,
        "image": "loc"
    },
    "На своей машине": {
        "message": "К сожалению, ты решил приехать на тренировку на автобусе, и машина стоит у дома."
                   " Ты уже опоздал на последний автобус, и не вернулся домой до 21:00."
                   " Взорвалась бомба, ты погиб. Начни сначала.",
        "dop_mes": None,
        "choices": ["Lose"],
        "scale": 0,
        "image": "loc"
    },
    "На автобусе": {
        "message": "В автобус зашла пожилая женщина. Что будешь делать?",
        "dop_mes": None,
        "choices": ["Уступить", "Не уступать"],
        "scale": 2,
        "image": "loc"
    },
    "На такси": {
        "message": "Ты потратил все деньги, но спокойно доехал до дома.",
        "dop_mes": "Вопрос 5: Ты приехал домой и захотел есть. Реши, что поесть",
        "choices": ["Съешь запечённую рыбу из холодильника", "Сваришь пельмени", "Закажешь еду из мака"],
        "scale": 5,
        "image": "loc"
    },
    "Уступить": {
        "message": "Ты уступил место, но тебя прижало, в давке,потеряв сознание."
                   " Ты не успел домой к 21:00, случился ядерный взрыв и ты погиб. Начни сначала.",
        "dop_mes": None,
        "choices": ["Lose"],
        "scale": 0,
        "image": "loc"
    },
    "Не уступать": {
        "message": "Ей уступил другой человек, и ты спокойно доехал, до дома",
        "dop_mes": "Вопрос 5: Ты приехал домой и захотел есть. Реши, что поесть",
        "choices": ["Съешь запечённую рыбу из холодильника", "Сваришь пельмени", "Закажешь еду из мака"],
        "scale": 1,
        "image": "loc"
    },
    "Съешь запечённую рыбу из холодильника": {
        "message": "Ты забыл, что у тебя аллергия на рыбу и съел ее. Ты отравился. Начни день сначала.",
        "dop_mes": None,
        "choices": None,
        "scale": 0,
        "image": "loc"
    },
    "Сваришь пельмени": {
        "message": "Ты открыл пачку пельменей и увидел номер карты 5536914163507944, отправил донат, поел и лег спать.",
        "dop_mes": "Сегодня ты смог окунуться в мир Кирилла"
                   " и пройти через все испытания, которые он преодолевал на своем пути."
                   " Теперь же пришло время узнать, насколько хорошо ты справился с этой задачей."
                   " Давай посмотрим на результаты твоего захватывающего приключения!",
        "choices": ["Узнать результаты"],
        "scale": 5,
        "image": "loc"
    },
    "Закажешь еду из мака": {
        "message": "Ты перепутал чикенбургер с фишбургером, а у тебя аллергия на рыбу. Ты погиб. Начни сначала.",
        "dop_mes": None,
        "choices": None,
        "scale": 0,
        "image": "loc"
    },
    "Узнать результаты": {
        "message": None,
        "dop_mes": None,
        "choices": ["itog"],
        "scale": 0,
        "image": "loc"
    },
    "Плохая концовка": {
        "message": "Ты просыпаешься в той же комнате."
                   " Тебе удалось выжить, но не удалось вернуться в своё тело."
                   " Начни день сначала и может в этот раз тебе повезёт!",
        "dop_mes": None,
        "choices": ["itog"],
        "scale": 0,
        "image": "loc"
    },
    "Хорошая концовка": {
        "message": "Ты просыпаешься в своей комнате."
                   " Поздравляем, тебе удалось прожить день Кирилла Казакова."
                   " Всё прошло по канону. Ты перевёл донат, ядерная бомба не взрывалась."
                   " А вы обратно поменялись телами.",
        "dop_mes": None,
        "choices": ["itog"],
        "scale": 0,
        "image": "loc"
    }
}