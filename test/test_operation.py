import pytest
from src.operation import Operation


def test_operation_instance(operation_class_fixture):
    """ Функция проверки создания экземпляра Operation """

    assert operation_class_fixture[0].from_type == "Счет"
    assert operation_class_fixture[0].from_number == "41421565395219882431"
    assert operation_class_fixture[0].from_number_encript == "**2431"
    assert operation_class_fixture[0].to_type == "Visa Classic"
    assert operation_class_fixture[0].to_number == "6831982476737658"
    assert operation_class_fixture[0].to_number_encript == "6831 98** **** 7658"
    assert operation_class_fixture[0].date == "23.03.2018"

    # Отсутствует поле from
    assert operation_class_fixture[1].from_type == ""
    assert operation_class_fixture[1].from_number == ""
    assert operation_class_fixture[1].from_number_encript == ""

def test_operation_status(operation_class_fixture):
    """ Проверка вывода стутуса операции """

    assert operation_class_fixture[0].get_status() == "23.03.2018 Открытие вклада\n" \
            "Счет **2431 -> Visa Classic 6831 98** **** 7658\n" \
            "48223.05 руб.\n"

    # Отсутствует поле from
    assert operation_class_fixture[1].get_status() == "18.07.2019 Перевод с карты на карту\n" \
            "  -> МИР 2956 60** **** 3342\n" \
            "82139.20 руб.\n"
