# Данные для pytest
import pytest
from src.operation import Operation


@pytest.fixture
def operation_class_fixture():
    return [Operation(
                pk=587085106,
                state="EXECUTED",
                date_time="2018-03-23T10:45:06.972075",
                amount="48223.05",
                currency="руб.",
                description="Открытие вклада",
                to="Visa Classic 6831982476737658",
                from_="Счет 41421565395219882431"
            ),
            Operation(
                pk=917824439,
                state="EXECUTED",
                date_time="2019-07-18T12:27:13.355343",
                amount="82139.20",
                currency="руб.",
                description="Перевод с карты на карту",
                to="МИР 2956603572573342"
            )]
