# Пример для карты
# Visa Platinum 7000792289606361  # входной аргумент
# Visa Platinum 7000 79** **** 6361  # выход функции

# Пример для счета
# Счет 73654108430135874305  # входной аргумент
# Счет **4305  # выход функции


def mask_account_card(my_str: str) -> str:
    """Маскирует номер карты по шаблону BANK-NAME XXXX XX** **** XXXX
    Маскирует номер счета по шаблону Счет **4305  # выход функции"""
    if "Счет" in my_str:
        masked_sch = "Счет" + " " + "**" + my_str[-4:-1] + my_str[-1]
        return masked_sch
    else:
        bank_name = ""
        for i in my_str:
            if i.isalpha() or i.isspace():
                bank_name += i
        bank_name = bank_name.strip()
        number_cart = my_str[-17:-1] + my_str[-1]
        masked = (
            number_cart[1:5]
            + " "  # первые 4 цифры
            + number_cart[5:7]
            + "**"
            + " "  # следующие 2 цифры и **
            + "****"
            + " "  # четыре звездочки
            + number_cart[-4:-1]  # последние 4 цифры
            + number_cart[-1]
        )
        masked_full = bank_name + " " + masked
        return masked_full


# принимает на вход строку с датой в формате  "2024-03-11T02:26:18.671407"
# возвращает строку с датой в формате  "ДД.ММ.ГГГГ" ("11.03.2024")


def get_date(my_str: str) -> str:
"""Функция которая выводит дату в формате ДД.ММ.ГГГГ"""
    date_mask = my_str[8:10] + "." + my_str[5:7] + "." + my_str[0:4]
    return date_mask
