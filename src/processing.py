# Функция фильтр по статусу
#  На входе функции [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

# на выходе
# # Выход функции со статусом по умолчанию 'EXECUTED'
# [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
# {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
#
# # Выход функции, если вторым аргументов передано 'CANCELED'
# [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
# {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


from datetime import datetime
from typing import List, Dict


def filter_by_state(my_list: List[Dict[str, str]], state: str = "EXECUTED") -> List[Dict[str, str]]:
    """Функция принимает на вход список словарей с данными о банковских операциях и параметр state,
    возвращает новый список, содержащий только те словари,
    у которых ключ state содержит переданное в функцию значение"""
    return [operation for operation in my_list if operation.get("state") == state]


# Функция сортировка по дате
# На входе [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
# {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
# {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
# {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
# Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
# [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
# {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
# {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
# {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


def sort_by_date(my_list: List[Dict[str, str]], reverse: bool = True) -> List[Dict[str, str]]:
    """Функция принимает на вход список словарей и параметр порядка сортировки,
    возвращает новый список, в котором исходные словари отсортированы по дате"""
    return sorted(my_list, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)
