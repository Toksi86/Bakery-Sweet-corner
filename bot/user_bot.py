from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from vk_api.utils import get_random_id


class Bot:
    def __init__(self, user_id):
        self.user_id = user_id
        self.category = None

    def create_start_button(self):
        keyboard = VkKeyboard(one_time=True, inline=False)
        keyboard.add_button(label="Начать", color="primary")
        return keyboard.get_keyboard()

    def create_back_button(self):
        keyboard = VkKeyboard(one_time=True, inline=False)
        keyboard.add_button(
            label="Главное меню", color=VkKeyboardColor.NEGATIVE
        )
        keyboard.add_line
        keyboard.add_button(
            label=f"{self.category}", color=VkKeyboardColor.NEGATIVE
        )
        return keyboard.get_keyboard()

    def send_start_button(self, vk):
        message = "Добро пожаловать! Выбреите категорию товаров"
        keyboard = self.create_start_button()
        self.send_message(vk, message, keyboard)

    def create_keyboard_lables(self, buttons):
        keyboard = VkKeyboard(one_time=True, inline=False)
        item_names = [item for item in buttons]

        for button in item_names:
            keyboard.add_button(label=button, color="primary")

            if button != buttons[-1]:
                keyboard.add_line()

        return keyboard.get_keyboard()

    def send_message(self, vk, message, keyboard=None):
        vk.messages.send(
            user_id=self.user_id,
            message=message,
            random_id=get_random_id(),
            keyboard=keyboard,
        )

    def send_category_menu(self, vk, category_names):
        keyboard = self.create_keyboard_lables(category_names)
        message = "Выберите категорию товаров"
        self.send_message(vk, message, keyboard)

    def send_product_menu(self, vk, product_names):
        keyboard = self.create_keyboard_lables(product_names)
        message = "Выберите карточку товара"
        self.send_message(vk, message, keyboard)

    def send_product_info(self, vk, product):
        keyboard = self.create_back_button()
        message = f"{product["name"]} \nОписание товара:\n{product['description']}\nФото"
        self.send_message(vk, message, keyboard)
