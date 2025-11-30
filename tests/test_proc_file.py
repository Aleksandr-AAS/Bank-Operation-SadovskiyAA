from src.proc_file import processing_csv
from src.proc_file import processing_xls
from unittest import mock
from unittest.mock import patch
import pandas as pd
import pytest


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
    mock_read_excel.return_value = transaction
    result = processing_xls("TEST.xlsx")
    assert result == transaction.to_dict("records")
    mock_read_excel.assert_called_once_with("TEST.xlsx")
