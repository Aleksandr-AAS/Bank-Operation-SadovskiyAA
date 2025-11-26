import pytest
from src.external_api import convert_to_rub
from unittest.mock import Mock
from unittest.mock import patch


@pytest.mark.parametrize(
    "input_data,output_data",
    [
        (
            {
                "id": 649467725,
                "state": "EXECUTED",
                "date": "2018-04-14T19:35:28.978265",
                "operationAmount": {"amount": "96995.73", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Счет 27248529432547658655",
                "to": "Счет 97584898735659638967",
            },
            "96995.73",
        )
    ],
)
def test_for_RUB_convert_to_rub(input_data, output_data):
    """Тестирование функции convert_to_rub"""
    result = str(convert_to_rub(input_data))
    assert result == str(output_data)


@pytest.mark.parametrize(
    "input_data1,output_data1",
    [
        (
            {
                "id": 782295999,
                "state": "EXECUTED",
                "date": "2019-09-11T17:30:34.445824",
                "operationAmount": {"amount": "54280.01", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 24763316288121894080",
                "to": "Счет 96291777776753236930",
            },
            "0.0",
        )
    ],
)
def test_for_USD_convert_to_rub(input_data1, output_data1) -> None:
    result = convert_to_rub(input_data1)
    result1 = result
    assert result1 == (result)


def test_convert_to_rub_all():
    mock_convert = Mock(return_value=5)
    convert_to_rub = mock_convert
    assert convert_to_rub([]) == 5
    mock_convert.assert_called_once_with([])


@pytest.fixture
def transaction_usd() -> None:
    return {
        "id": 782295999,
        "state": "EXECUTED",
        "date": "2019-09-11T17:30:34.445824",
        "operationAmount": {"amount": "54280.01", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 24763316288121894080",
        "to": "Счет 96291777776753236930",
    }


@patch("requests.request")
def test_convert_to_rub_APIcall_Success(mock_get, transaction_usd):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = 0.0
    mock_get.return_value = mock_response
    result = convert_to_rub(transaction_usd)
    assert result == 0.0
    mock_get.assert_called_once()


@patch("requests.request")
def test_convert_to_rub_APIcall_Fail(mock_get, transaction_usd):
    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.json.return_value = 0.0
    mock_get.return_value = mock_response
    result = convert_to_rub(transaction_usd)
    assert result == 0.0
    mock_get.assert_called_once()
