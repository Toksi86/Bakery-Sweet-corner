import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_PATH = os.getenv("API_PATH")


def get_categories() -> list[dict]:
    url = f"{API_PATH}/categories"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Ошибка: {response.status_code}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def get_products_in_category(name) -> list[dict]:
    url = f"{API_PATH}/categories/{name}/products"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()

        else:
            print(f"Ошибка: {response.status_code}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def get_products() -> list[dict]:
    url = f"{API_PATH}/products/"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()

        else:
            print(f"Ошибка: {response.status_code}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def get_product(name) -> list[dict]:
    url = f"{API_PATH}/products/{name}/"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()[0]

        else:
            print(f"Ошибка: {response.status_code}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
