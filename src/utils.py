import json
import logging
#
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(
    "C:/Users/1/PycharmProjects/Bank-Operation-SadovskiyAA/logs/utils.log", mode="w", encoding="utf-8"
)
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
