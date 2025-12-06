import csv
import os
import re
from collections import Counter

import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))

csv_file_path = os.path.join(current_dir, "../data/transactions.csv")
csv_file_path_real = os.path.abspath(csv_file_path)  # Это путь до csv

xls_file_path = os.path.join(current_dir, "../data/transactions_excel.xlsx")
xls_file_path_real = os.path.abspath(xls_file_path)  # Это путь до xls


def processing_csv(file_path: str) -> list[dict]:
    """Функция  считывания финансовых операций из CSV выдает список словарей с транзакциями"""
    try:
        with open(file_path, mode="r", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=";")
            result = [row for row in csv_reader]
        return result
    except FileNotFoundError:
        return []


def processing_xls(file_path: str) -> list[dict]:
    """Функция  считывания финансовых операций из XLS выдает список словарей с транзакциями"""
    try:
        df = pd.read_excel(file_path)
        df = df.fillna("")
        if "description" in df.columns:
            df["description"] = df["description"].astype(str)
        result = df.to_dict("records")
        return result
    except FileNotFoundError:
        return []


def process_bank_search(data: list[dict], input_desc: str):
    """Функция принимает список словарей с данными о банковских операциях и строку поиска
    возвращает список словарей, у которых в описании есть данная строка"""
    pattern = re.escape(input_desc)
    out_data = []
    for transaction in data:
        description = transaction.get("description", "")
        if not isinstance(description, str):
            description = str(description) if description is not None else ""
        if re.search(pattern, description, re.IGNORECASE):
            out_data.append(transaction)
    return out_data


# print(processing_xls(xls_file_path_real))

cat = {"Перевод со счета на счет", "Перевод с карты на карту"}


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    возвращает словарь, в котором ключи — это названия категорий,
    значения — это количество операций в каждой категории."""
    if not data or not categories:
        return {}
    categories_lower = {cat.lower(): cat for cat in categories}
    counter = Counter()
    for operation in data:
        if not isinstance(operation, dict):
            continue
        description = operation.get("description", "")
        if not isinstance(description, str):
            continue
        desc_lower = description.lower()
        for cat_lower, original_cat in categories_lower.items():
            if cat_lower in desc_lower:
                counter[original_cat] += 1
                break
    return {category: counter[category] for category in categories}


# print(process_bank_operations(processing_xls(xls_file_path_real),cat))
