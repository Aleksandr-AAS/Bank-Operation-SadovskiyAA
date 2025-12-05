from unittest import mock
from unittest.mock import patch

import pandas as pd
import pytest

from src.proc_file import process_bank_operations, process_bank_search, processing_csv, processing_xls


@pytest.fixture
def transaction():
    return pd.DataFrame(
        {
            "id": 782295999,
            "state": "EXECUTED",
            "date": "2019-09-11T17:30:34.445824",
            "operationAmount": {"amount": "54280.01", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 24763316288121894080",
            "to": "Счет 96291777776753236930",
        }
    )


def test_processing_csv(transaction):
    """Тестирование функции processing_csv"""
    csv_string = transaction.to_csv(sep=";", index=False)
    with mock.patch("builtins.open", mock.mock_open(read_data=csv_string)) as open_:
        result = processing_csv("TEST.csv")
        assert result == [
            {
                "date": "2019-09-11T17:30:34.445824",
                "description": "Перевод организации",
                "from": "Счет 24763316288121894080",
                "id": "782295999",
                "operationAmount": "54280.01",
                "state": "EXECUTED",
                "to": "Счет 96291777776753236930",
            },
            {
                "date": "2019-09-11T17:30:34.445824",
                "description": "Перевод организации",
                "from": "Счет 24763316288121894080",
                "id": "782295999",
                "operationAmount": "{'name': 'USD', 'code': 'USD'}",
                "state": "EXECUTED",
                "to": "Счет 96291777776753236930",
            },
        ]
        open_.assert_called_once_with("TEST.csv", mode="r", encoding="utf-8")


@patch("pandas.read_excel")
def test_processing_xls(mock_read_excel, transaction):
    """Тестирование функции processing_xls"""
    mock_read_excel.return_value = transaction
    result = processing_xls("TEST.xlsx")
    assert result == transaction.to_dict("records")
    mock_read_excel.assert_called_once_with("TEST.xlsx")


@pytest.fixture
def transactions_list():
    return [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 3598919.0,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 593027.0,
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "amount": 30368.0,
            "currency_name": "Shilling",
            "currency_code": "TZS",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
            "description": "Перевод с карты на карту",
        },
    ]


def test_process_bank_search(transactions_list):
    """Тестирование функции process_bank_search"""
    assert process_bank_search(transactions_list, "Перевод организации")[0] == transactions_list[0]
    list = []
    list.append(transactions_list[1])
    list.append(transactions_list[2])
    assert process_bank_search(transactions_list, "Перевод с карты на карту") == list
    assert process_bank_search(transactions_list, "Chto-to poshlo ne tak") == []


def test_process_bank_operations(transactions_list):
    """Тестирование функции process_bank_operations"""
    list = ["Перевод организации", "Перевод с карты на карту"]
    assert process_bank_operations(transactions_list, list) == {
        "Перевод организации": 1,
        "Перевод с карты на карту": 2,
    }
    list = ["Chto-to poshlo ne tak"]
    assert process_bank_operations(transactions_list, list) == {"Chto-to poshlo ne tak": 0}
    assert process_bank_operations([], list) == {}
    list = []
    assert process_bank_operations(transactions_list, list) == {}
