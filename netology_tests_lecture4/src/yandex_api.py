# src/yandex_api.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("YANDEX_TOKEN")
BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"
HEADERS = {
    "Authorization": f"OAuth {TOKEN}",
    "Content-Type": "application/json"
}


def create_folder(path: str) -> dict:
    """Создаёт папку на Яндекс.Диске"""
    params = {"path": path}
    response = requests.put(f"{BASE_URL}", headers=HEADERS, params=params)
    return {
        "status_code": response.status_code,
        "json": response.json() if response.content else None,
        "response": response
    }


def get_folder_info(path: str) -> dict:
    """Получает информацию о папке"""
    params = {"path": path}
    response = requests.get(f"{BASE_URL}", headers=HEADERS, params=params)
    return {
        "status_code": response.status_code,
        "json": response.json() if response.content else None,
        "exists": response.status_code == 200
    }


def delete_folder(path: str) -> int:
    """Удаляет папку с Яндекс.Диска"""
    params = {"path": path, "permanent": "true"}
    response = requests.delete(f"{BASE_URL}", headers=HEADERS, params=params)
    return response.status_code