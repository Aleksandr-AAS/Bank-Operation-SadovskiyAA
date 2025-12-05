import json
import logging
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, "../logs/utils.log")
abs_file_path = os.path.abspath(rel_file_path)  # Это путь до лог файла

json_file_path = os.path.join(current_dir, "../data/operations.json")
json_file_path_real = os.path.abspath(json_file_path)  # Это путь до json файла


logger = logging.getLogger("utils.py")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(abs_file_path, mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_list_dict_json(file_path: str) -> list[dict]:
    """
    Загружает список транзакций из JSON-файла. Функция принимает-путь до JSON-файла(с именем файла),
    возвращает-список словарей с данными о транзакциях или пустой список
    """
    logger.info("Вызов функции")
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        if isinstance(data, list):
            logger.info("Файл успешно прочитан, данные выведены")
            return data
        else:
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error("Неправильный формат файла или файл не найден")
        return []


# print(get_list_dict_json(json_file_path_real))
