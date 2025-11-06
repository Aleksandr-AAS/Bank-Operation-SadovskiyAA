import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def input_data() -> None:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.mark.parametrize(
    "count, result",
    [
        (
            5,
            [
                "Перевод организации",
                "Перевод со счета на счет",
                "Перевод со счета на счет",
                "Перевод с карты на карту",
                "Перевод организации",
            ],
        ),
        (
            3,
            [
                "Перевод организации",
                "Перевод со счета на счет",
                "Перевод со счета на счет",
            ],
        ),
        (0, []),
    ],
)
def test_transaction_descriptions(count, result, input_data):
    """Тестирование функции transaction_descriptions используя параметризацию и фикстуры"""
    descriptions = list(transaction_descriptions(input_data))
    assert descriptions[:count] == list(result)


@pytest.mark.parametrize(
    "count1, result1",
    [
        (0, []),
        (
            1,
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ],
        ),
    ],
)
def test_filter_by_currency(count1, result1, input_data):
    """Тестирование функции filter_by_currency используя параметризацию и фикстуры"""
    descriptions = list(filter_by_currency(input_data, "USD"))
    assert descriptions[:count1] == list(result1)


@pytest.mark.parametrize(
    "count2, result2",
    [(1, ["0000 0000 0000 0001"])],
)
def test_card_number_generator(count2, result2):
    """Тестирование функции fcard_number_generator используя параметризацию"""
    descriptions = list(card_number_generator(1, 1))
    assert descriptions[:count2] == result2
