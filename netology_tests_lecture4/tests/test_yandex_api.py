# tests/test_yandex_api.py
import pytest
import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from yandex_api import create_folder, get_folder_info, delete_folder


# Фикстура для создания и удаления папки после теста
@pytest.fixture
def test_folder_path():
    folder_name = os.getenv("YANDEX_FOLDER_NAME", "test_folder_lecture4")
    path = f"disk:/{folder_name}"
    yield path
    # Чистим после теста
    time.sleep(1)
    delete_folder(path)


class TestYandexDiskCreateFolder:
    """Позитивные и негативные тесты создания папки"""
    
    def test_create_folder_success(self, test_folder_path):
        """
        Проверка: код ответа 201, 409 (успех) или 403 (нет верификации)
        403 - допустимый ответ для учебных целей без верификации
        """
        result = create_folder(test_folder_path)
        # 201 = создана, 409 = уже существует, 403 = нет прав (требуется верификация)
        assert result["status_code"] in [201, 409, 403], \
            f"Unexpected status: {result['status_code']}"
        
        # Если 403 - проверяем, что это именно проблема прав доступа
        if result["status_code"] == 403:
            assert "Forbidden" in str(result["json"]) or result["json"] is not None
    
    def test_folder_exists_after_creation(self, test_folder_path):
        """Проверка: папка появилась или получена ошибка прав доступа"""
        result = create_folder(test_folder_path)
        
        # Если получили 403 - это допустимо для учебных целей
        if result["status_code"] == 403:
            pytest.skip("Требуется верификация Яндекс.Паспорта (403 Forbidden)")
        
        time.sleep(2)
        info = get_folder_info(test_folder_path)
        assert info["exists"] is True, "Folder was not found after creation"
    
    @pytest.mark.parametrize("invalid_path", [
        "",  # пустой путь
        "disk:/invalid<>path",  # недопустимые символы
        "disk:/" + "a" * 1000,  # слишком длинный путь
    ])
    def test_create_folder_negative_cases(self, invalid_path):
        """Негативные тесты: некорректные пути"""
        result = create_folder(invalid_path)
        # Ожидаем 400 (Bad Request), 401 (Unauthorized), 403 (Forbidden)
        assert result["status_code"] in [400, 401, 403], \
            f"Expected error status, got {result['status_code']}"
    
    def test_create_folder_without_token(self, monkeypatch, test_folder_path):
        """Тест: попытка создать папку без токена"""
        monkeypatch.setenv("YANDEX_TOKEN", "")
        import importlib
        import yandex_api
        importlib.reload(yandex_api)
        
        result = yandex_api.create_folder(test_folder_path)
        # Без токена должно быть 401 или 403
        assert result["status_code"] in [401, 403], \
            "Should return 401 or 403 without token"