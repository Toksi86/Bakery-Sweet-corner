from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def create_keyboard(menu=None):
    keyboard = VkKeyboard(one_time=True, inline=False)
    if menu is None:
        menu = []
    for button in menu:
        keyboard.add_button(label=button, color="primary")

        if button != menu[-1]:
            keyboard.add_line()

    if menu:
        keyboard.add_line()
    keyboard.add_button(label="Главное меню", color=VkKeyboardColor.NEGATIVE)

    return keyboard.get_keyboard()
