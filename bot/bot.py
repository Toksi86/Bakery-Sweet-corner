import os

import vk_api
from dotenv import load_dotenv
from vk_api.keyboard import VkKeyboard
from vk_api.longpoll import VkEventType, VkLongPoll

load_dotenv()

TOKEN = os.getenv("TOKEN")


vk_session = vk_api.VkApi(token=TOKEN)

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()


print("Бот запущен!")


def generate_buttons(buttons):
    keyboard = VkKeyboard(one_time=True, inline=False)

    for category in buttons:
        keyboard.add_button(label=category, color="primary")

        if category != buttons[-1]:
            keyboard.add_line()

    # Кнопка 'Назад'
    # keyboard.add_line()
    # eyboard.add_button(label='Назад', color=VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()


def check_start(event):
    if (
        event.type == VkEventType.MESSAGE_NEW
        and event.to_me
        and event.text == "Начать"
    ):
        vk.messages.send(
            user_id=event.user_id,
            message=f"Вы выбрали: {event.text}",
            random_id=vk_api.utils.get_random_id(),
            keyboard=category_keyboard,
        )


def check_choose_category(event):
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        if event.text == "Выпечка":
            baking_keyboard = generate_buttons(baking_menu)
            action_category(event, baking_menu, baking_keyboard)
        elif event.text == "Десерты":
            desserts_category = generate_buttons(desserts_menu)
            action_category(event, desserts_menu, desserts_category)
        elif event.text == "Напитки":
            drinks_category = generate_buttons(drinks_menu)
            action_category(event, drinks_menu, drinks_category)


categories = ["Выпечка", "Десерты", "Напитки"]

baking_menu = ["Круасан", "Штрудель", "Рогалик"]
drinks_menu = ["Кофе", "Чай", "Морс"]
desserts_menu = ["Чизкейк", "Медовик", "Муравейник"]

category_keyboard = generate_buttons(categories)


def action_category(event, menu, keyboard=None):
    start_pos = 1
    message = ""
    for food in menu:
        message += f"{start_pos}. {food} \n"
        start_pos += 1
    vk.messages.send(
        user_id=event.user_id,
        message=message,
        random_id=vk_api.utils.get_random_id(),
        keyboard=keyboard,
    )


while True:
    try:
        for event in longpoll.listen():
            check_start(event)
            check_choose_category(event)

    except KeyboardInterrupt:
        print("Бот остановлен")
        break
    except Exception as e:
        print(f"Произошла ошибка: {e}")
