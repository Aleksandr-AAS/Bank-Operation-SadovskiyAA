from src.proc_file import  processing_csv, processing_xls
from src.utils import get_list_dict_json
import os
from typing import List
from datetime import datetime

current_dir = os.path.dirname(os.path.abspath(__file__))

csv_file_path = os.path.join(current_dir, "../data/transactions.csv")
csv_file_path_real = os.path.abspath(csv_file_path)  # Это путь до csv

xls_file_path = os.path.join(current_dir, "../data/transactions_excel.xlsx")
xls_file_path_real = os.path.abspath(xls_file_path)  # Это путь до xls

json_file_path = os.path.join(current_dir, "../data/operations.json")
json_file_path_real = os.path.abspath(json_file_path)  # Это путь до json файла


def main_menu():
    """Главное меню программы для работы с банковскими транзакциями."""
    menu_text = """
    Привет! Добро пожаловать в программу работы 
    с банковскими транзакциями. 
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    4. Выход
    """

    while True:
        print(menu_text)

        try:
            choice = input("Введите номер пункта меню (1-4): ").strip()
            if choice == "1":
                print("Вы выбрали: Получить информацию о транзакциях из JSON-файла")
                input_status = get_operation_status_filter()
                transaction = get_list_dict_json(json_file_path_real)
                filtered_transactions = filter_by_status(transaction, input_status)
                if ask_yes_no_question("Отсортировать операции по дате?"):
                    sort_order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
                    if "убыван" in sort_order in sort_order:
                        filtered_transactions = sort_transactions(filtered_transactions, reverse=True)
                    else:
                        filtered_transactions = sort_transactions(filtered_transactions, reverse=False)
                if ask_yes_no_question("Выводить только рублевые транзакции?"):
                    filtered_transactions = filter_by_currency(filtered_transactions, "RUB")
                if ask_yes_no_question(
                    "Отфильтровать список транзакций по определенному слову в описании?"
                    "\n -Открытие вклада-\n -Перевод организации- \n -Перевод с карты на карту-\n"
                ):
                    keyword = input("Введите ключевое слово для поиска в описании: ").strip()
                    if keyword:
                        filtered_transactions = filter_by_description(filtered_transactions, keyword)
                print("\n" + "=" * 50)
                print("Распечатываю итоговый список транзакций...")
                print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
                print("=" * 50)
                if filtered_transactions:
                    for i, transaction in enumerate(filtered_transactions, 1):
                        print(f"\nОперация #{i}:")
                        print(f"  ID: {transaction.get('id')}")
                        print(f"  Дата: {transaction.get('date')}")
                        print(f"  Сумма: {transaction.get('amount')} {transaction.get('currency_name')}")
                        print(f"  От: {transaction.get('from', 'Не указано')}")
                        print(f"  Кому: {transaction.get('to')}")
                        print(f"  Описание: {transaction.get('description')}")
                else:
                    print("Нет транзакций, соответствующих критериям фильтрации.")
                    print("\n" + "=" * 50)

            elif choice == "2":
                print("Вы выбрали: Получить информацию о транзакциях из CSV-файла")
                input_status = get_operation_status_filter()
                transaction = processing_csv(csv_file_path_real)
                filtered_transactions = filter_by_status(transaction, input_status)
                if ask_yes_no_question("Отсортировать операции по дате?"):
                    sort_order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
                    if "убыван" in sort_order in sort_order:
                        filtered_transactions = sort_transactions(filtered_transactions, reverse=True)
                    else:
                        filtered_transactions = sort_transactions(filtered_transactions, reverse=False)
                if ask_yes_no_question("Выводить только рублевые транзакции?"):
                    filtered_transactions = filter_by_currency(filtered_transactions, "RUB")
                if ask_yes_no_question(
                    "Отфильтровать список транзакций по определенному слову в описании?"
                    "\n -Открытие вклада-\n -Перевод организации- \n -Перевод с карты на карту-\n"
                ):
                    keyword = input("Введите ключевое слово для поиска в описании: ").strip()
                    if keyword:
                        filtered_transactions = filter_by_description(filtered_transactions, keyword)
                print("\n" + "=" * 50)
                print("Распечатываю итоговый список транзакций...")
                print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
                print("=" * 50)
                if filtered_transactions:
                    for i, transaction in enumerate(filtered_transactions, 1):
                        print(f"\nОперация #{i}:")
                        print(f"  ID: {transaction.get('id')}")
                        print(f"  Дата: {transaction.get('date')}")
                        print(f"  Сумма: {transaction.get('amount')} {transaction.get('currency_name')}")
                        print(f"  От: {transaction.get('from', 'Не указано')}")
                        print(f"  Кому: {transaction.get('to')}")
                        print(f"  Описание: {transaction.get('description')}")
                else:
                    print("Нет транзакций, соответствующих критериям фильтрации.")
                    print("\n" + "=" * 50)

            elif choice == "3":
                print("Вы выбрали: Получить информацию о транзакциях из XLSX-файла")
                transaction = processing_xls(xls_file_path_real)
                filtered_transactions = filter_by_status(transaction, input_status)
                if ask_yes_no_question("Отсортировать операции по дате?"):
                    sort_order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
                    if "убыван" in sort_order in sort_order:
                        filtered_transactions = sort_transactions(filtered_transactions, reverse=True)
                    else:
                        filtered_transactions = sort_transactions(filtered_transactions, reverse=False)
                if ask_yes_no_question("Выводить только рублевые транзакции?"):
                    filtered_transactions = filter_by_currency(filtered_transactions, "RUB")
                if ask_yes_no_question(
                    "Отфильтровать список транзакций по определенному слову в описании?"
                    "\n -Открытие вклада-\n -Перевод организации- \n -Перевод с карты на карту-\n"
                ):
                    keyword = input("Введите ключевое слово для поиска в описании: ").strip()
                    if keyword:
                        filtered_transactions = filter_by_description(filtered_transactions, keyword)
                print("\n" + "=" * 50)
                print("Распечатываю итоговый список транзакций...")
                print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
                print("=" * 50)
                if filtered_transactions:
                    for i, transaction in enumerate(filtered_transactions, 1):
                        print(f"\nОперация #{i}:")
                        print(f"  ID: {transaction.get('id')}")
                        print(f"  Дата: {transaction.get('date')}")
                        print(f"  Сумма: {transaction.get('amount')} {transaction.get('currency_name')}")
                        print(f"  От: {transaction.get('from', 'Не указано')}")
                        print(f"  Кому: {transaction.get('to')}")
                        print(f"  Описание: {transaction.get('description')}")
                else:
                    print("Нет транзакций, соответствующих критериям фильтрации.")

                    print("\n" + "=" * 50)

            elif choice == "4":
                print("Спасибо за использование программы! До свидания!")
                break

            else:
                print("Ошибка: пожалуйста, введите число от 1 до 4")

        except KeyboardInterrupt:
            print("\n\nПрограмма прервана пользователем. До свидания!")
            break
        except Exception as e:
            print(f"Произошла ошибка: {e}. Пожалуйста, попробуйте снова.")


def get_operation_status_filter():
    """
    Запрашивает у пользователя статус операций для фильтрации.
    Возвращает выбранный статус или None, если выбраны все статусы.
    """
    available_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    print("\n" + "=" * 60)
    print("Введите статус, по которому необходимо выполнить фильтрацию.")
    print("Доступные для фильтровки статусы:", ", ".join(available_statuses))
    print("Или введите 'ALL' для выбора всех статусов")
    print("Или введите 'EXIT' для возврата в предыдущее меню")
    print("=" * 60)

    while True:
        user_input = input("\nВведите статус операции: ").strip().upper()

        if user_input == "EXIT":
            print("Возврат в предыдущее меню...")
            return None

        if user_input == "ALL":
            print("Вы выбрали все статусы операций")
            return None

        if user_input in available_statuses:
            print(f"Вы выбрали статус: {user_input}")
            return user_input

        print(f"Ошибка: статус '{user_input}' недоступен.")
        print(f"Доступные статусы: {', '.join(available_statuses)}")
        print("Попробуйте снова.")


def filter_by_status(transactions: List[dict], status: str) -> List[dict]:
    """Фильтрует транзакции по статусу (с проверкой на None)."""
    if transactions is None or status is None:
        return []

    status_upper = status.upper()
    result = []

    for transaction in transactions:
        if transaction and isinstance(transaction, dict):
            trans_status = transaction.get("state")
            if trans_status and str(trans_status).upper() == status_upper:
                result.append(transaction)

    return result


def sort_transactions(transactions: List[dict], reverse: bool = False) -> List[dict]:
    """Сортирует транзакции по дате."""
    return sorted(
        transactions, key=lambda x: datetime.fromisoformat(x["date"].replace("Z", "+00:00")), reverse=reverse
    )


def ask_yes_no_question(question: str) -> bool:
    """Задает вопрос Да/Нет и возвращает булево значение."""
    while True:
        answer = input(f"{question} (Да/Нет): ").strip().lower()
        if answer in ["да", "д"]:
            return True
        elif answer in ["нет", "н"]:
            return False
        else:
            print("Пожалуйста, ответьте 'Да' или 'Нет'")


def filter_by_currency(transactions: List[dict], currency_code: str = "RUB") -> List[dict]:
    """Фильтрует транзакции по коду валюты."""
    if not transactions:
        return []
    currency_upper = currency_code.upper()
    return [
        t for t in transactions if t.get("currency_code") and str(t.get("currency_code")).upper() == currency_upper
    ]


def filter_by_description(transactions: List[dict], keyword: str) -> List[dict]:
    """Фильтрует транзакции по ключевому слову в описании."""
    if not transactions or not keyword:
        return transactions
    keyword_lower = keyword.lower()
    return [t for t in transactions if t.get("description") and keyword_lower in t.get("description", "").lower()]


main_menu()

