from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_account() -> None:
    assert get_mask_account(876543) == "**6543"


def test_get_mask_account_not_len():
    assert get_mask_account("") == "Номер счета должен содержать минимум 6 цифр"
    assert get_mask_account(87654) == "Номер счета должен содержать минимум 6 цифр"


def test_get_mask_card_number() -> None:
    assert get_mask_card_number(9876543210987654) == "9876 54** **** 7654"


def test_get_mask_card_number_not_len() -> None:
    assert get_mask_card_number(987654321098765) == "Номер карты должен содержать 16 цифр"
    assert get_mask_card_number(98765432109876541) == "Номер карты должен содержать 16 цифр"
    assert get_mask_card_number("") == "Номер карты должен содержать 16 цифр"
