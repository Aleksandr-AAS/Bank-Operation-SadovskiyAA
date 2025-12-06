import logging
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, "../logs/utils.log")
abs_file_path = os.path.abspath(rel_file_path)

logger = logging.getLogger("masks.log")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(abs_file_path, mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


# Функцию маскировки номера банковской карты
# 7000792289606361     # входной аргумент
# 7000 79** **** 6361  # выход функции


def get_mask_card_number(my_str: int) -> str:
    """Маскирует номер карты по шаблону XXXX XX** **** XXXX"""
    logger.info("Вызов функции - get_mask_card_number")
    my_str1 = str(my_str)
    # Проверяем корректность длины номера карты
    if len(my_str1) != 16:
        logger.error("Ошибка - Номер карты должен содержать 16 цифр")
        return "Номер карты должен содержать 16 цифр"
    # Формируем маску
    masked = (
        my_str1[0:4]
        + " "  # первые 4 цифры
        + my_str1[4:6]
        + "**"
        + " "  # следующие 2 цифры и **
        + "****"
        + " "  # четыре звездочки
        + my_str1[-4:-1]
        + my_str1[-1]  # последние 4 цифры
    )
    logger.info("Функция get_mask_card_number - успешно выполнена")
    return masked


# Функцию маскировки номера банковского счета
# 73654108430135874305  # входной аргумент
# **4305  # выход функции


def get_mask_account(my_str: int) -> str:
    """Маскирует номер счета по шаблону **XXXX"""
    # Преобразуем число в строку
    logger.info("Вызов функции - get_mask_account")
    my_str1 = str(my_str)
    # Проверяем минимальную длину номера счета
    if len(my_str1) < 6:
        logger.error("Ошибка - Номер счета должен содержать минимум 6 цифр")
        return "Номер счета должен содержать минимум 6 цифр"
    # Формируем маску
    masked = "**" + my_str1[-4:-1] + my_str1[-1]
    logger.info("Функция get_mask_account - успешно выполнена")
    return masked
