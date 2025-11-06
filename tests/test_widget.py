import pytest

from src.widget import get_date, mask_account_card


def test_get_date() -> None:
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("") == "Проверьте данные"


def test_mask_account_card() -> None:
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"
    assert mask_account_card("") == "Проверьте номер счета или карты"


@pytest.mark.parametrize(
    "input_data, out_data",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ],
)
def test_mask_account_card_1(input_data, out_data) -> None:
    assert mask_account_card(input_data) == out_data
