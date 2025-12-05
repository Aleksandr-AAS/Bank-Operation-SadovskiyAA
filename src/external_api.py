import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert_to_rub(transaction: dict) -> float:
    """Функция осуществляет конвертацию суммы транзакции в рубли"""
    try:
        amount = transaction["operationAmount"]["amount"]
        currency = transaction["operationAmount"]["currency"]["code"]

        if currency != "RUB":
            url = f"https://api.apilayer.com/exchangerates_data/convert?to={"RUB"}&from={currency}&amount={amount}"
            headers = {"apikey": API_KEY}
            response = requests.request("GET", url, headers=headers)
            status_code = response.status_code
            result = response.json()
            if status_code == 200:
                return float(result["result"])
            else:
                return 0.0
        else:
            return float(amount)
    except Exception as e:
        print(f"Ошибка конвертации: {e} {status_code}")
        return 0.0
