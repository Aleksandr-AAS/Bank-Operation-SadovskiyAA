import csv
import pandas as pd


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
        result = df.to_dict("records")
        return result
    except FileNotFoundError:
        return []
