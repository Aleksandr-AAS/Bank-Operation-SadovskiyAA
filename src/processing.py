
from datetime import datetime
from typing import List, Dict


def filter_by_state(my_list: List[Dict[str, str]], state: str = "EXECUTED") -> List[Dict[str, str]]:
    """
    Функция принимает на вход список словарей с данными о банковских операциях и параметр state,
    возвращает новый список, содержащий только те словари,
    у которых ключ state содержит переданное в функцию значение
    """
    for operation in my_list:
        if operation.get("state") == '':
            return "Проверьте даные"

    return [operation for operation in my_list if operation.get("state") == state]


def sort_by_date(my_list: List[Dict[str, str]], reverse: bool = True) -> List[Dict[str, str]]:
    """
    Функция принимает на вход список словарей и параметр порядка сортировки,
    возвращает новый список, в котором исходные словари отсортированы по дате
    """
    for operation in my_list:
        if operation.get("date") == '':
            return "Проверьте даные"

    return sorted(my_list, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)
