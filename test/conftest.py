# Данные для pytest
import pytest
from src.operation import Operation


@pytest.fixture
def operation_fixture():
    return [Operation(
            pk=587085106,
            state="EXECUTED",
            date_time="2018-03-23T10:45:06.972075",
            amount="48223.05",
            currency="руб.",
            description="Открытие вклада",
            from_="Счет 41421565395219882431",
            to="Visa Classic 6831982476737658"
        ),
        Operation(
            pk=917824439,
            state="EXECUTED",
            date_time="2019-07-18T12:27:13.355343",
            amount="82139.20",
            currency="руб.",
            description="Перевод с карты на карту",
            to="МИР 2956603572573342"
        ),
        Operation(
            pk=121646999,
            state="CANCELED",
            date_time="2018-06-08T16:14:59.936274",
            amount="91121.62",
            currency="руб.",
            description="Перевод организации",
            from_="Maestro 7552745726849311",
            to="Счет 34799481846914116850"
        ),
        Operation(
            pk=816266176,
            state="CANCELED",
            date_time="2018-06-24T00:46:32.422648",
            amount="60030.73",
            currency="руб.",
            description="Перевод организации",
            from_="МИР 6381702861749111",
            to="Счет 27804394774631586026"
        ),
        Operation(
            pk=736942989,
            state="EXECUTED",
            date_time="2019-09-06T00:48:01.081967",
            amount="6357.56",
            currency="руб.",
            description="Перевод организации",
            from_="Visa Gold 3654412434951162",
            to="Счет 59986621134048778289"
        ),
        Operation(
            pk=888407131,
            state="EXECUTED",
            date_time="2019-09-29T14:25:28.588059",
            amount="45849.53",
            currency="руб.",
            description="Перевод со счета на счет",
            from_="Счет 35421428450077339637",
            to="Счет 46723050671868944961"
        ),
        Operation(
            pk=634356296,
            state="EXECUTED",
            date_time="2018-01-21T01:10:28.317704",
            amount="96900.90",
            currency="руб.",
            description="Перевод со счета на счет",
            from_="Счет 33407225454123927865",
            to="Счет 79619011266276091215"
        )]
