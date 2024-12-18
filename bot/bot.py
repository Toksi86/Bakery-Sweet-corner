import os

import vk_api
from bot_requests import (
    get_categories,
    get_product,
    get_products,
    get_products_in_category,
)
from dotenv import load_dotenv
from user_bot import Bot
from vk_api.longpoll import VkEventType, VkLongPoll

#  from vk_api.upload import VkUpload

load_dotenv()

TOKEN = os.getenv("TOKEN")
GROUP_ID = os.getenv("GROUP_ID")
ALBUM_ID = os.getenv("ALBUM_ID")

vk_session = vk_api.VkApi(token=TOKEN)

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

bots: dict[Bot] = {}


def get_items_name(data):
    item_names = [item["name"] for item in data]
    return item_names


def get_product_names():
    products = get_products()
    product_names = get_items_name(products)
    return product_names


def get_product_names_in_category(category_name):
    products_in_category = get_products_in_category(category_name)
    product_names_in_categry = get_items_name(products_in_category)
    return product_names_in_categry


def get_category_names():
    category = get_categories()
    category_names = get_items_name(category)
    return category_names


# def send_photo(user_id, product_name, caption=None):
#    upload = VkUpload(vk_session)
#    photo_path = get_path(product_name)
#    album_id = create_or_get_album()
#    photo = upload.photo(photo_path, album_id=album_id, group_id=GROUP_ID)
#    owner_id = photo[0]["owner_id"]
#    photo_id = photo[0]["id"]
#    attachment = f"photo{owner_id}_{photo_id}"
#    vk.messages.send(
#        user_id=user_id,
#        random_id=vk_api.utils.get_random_id(),
#        attachment=attachment,
#        message=caption,
#    )
#
#
# def create_or_get_album():
#    try:
#        response = vk.photos.createAlbum(
#            title="Десерты",
#            description="Альбом для товаров",
#            upload_by_admins_only=True,
#            comments_disabled=False,
#            messages_disabled=False,
#        )
#        album_id = response["id"]
#    except vk_api.exceptions.ApiError as e:
#        print(f"Ошибка при создании альбома: {e}")
#        albums = vk.photos.getAlbums(owner_id=GROUP_ID)
#        for album in albums["items"]:
#            if album["title"] == "Десерты":
#                album_id = album["id"]
#                break
#    return album_id


def check_get_message(event):
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        if event.text == "Начать" or event.text == "Главное меню":
            categories_names = get_category_names()
            bots[event.user_id].send_category_menu(vk, categories_names)
            bots[event.user_id].category = None
        if event.text in get_category_names():
            bots[event.user_id].send_product_menu(
                vk, get_product_names_in_category(event.text)
            )
            bots[event.user_id].category = event.text
        if event.text in get_product_names():
            bots[event.user_id].send_product_info(vk, get_product(event.text))


def check_first_time(event):
    if event.user_id not in bots:
        bots[event.user_id] = Bot(event.user_id)
        bots[event.user_id].send_start_button(vk)


while True:
    try:
        for event in longpoll.listen():
            check_first_time(event)
            check_get_message(event)
    except KeyboardInterrupt:
        print("Бот остановлен")
        break
    except Exception as e:
        print(f"Произошла ошибка: {e}")
