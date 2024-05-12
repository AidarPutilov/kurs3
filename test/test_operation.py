from src.operation import Operation


def test_operation_instance():

    op = Operation(
        pk=587085106,
        state="EXECUTED",
        date_time="2018-03-23T10:45:06.972075",
        amount="48223.05",
        currency="руб.",
        description="Открытие вклада",
        from_="Счет 41421565395219882431",
        to="Visa Classic 6831982476737658"
    )

    assert op.from_type == "Счет"
    assert op.from_number == "41421565395219882431"
    assert op.from_number_encript == "**2431"
    assert op.to_type == "Visa Classic"
    assert op.to_number == "6831982476737658"
    assert op.to_number_encript == "6831 98** **** 7658"
    assert op.date == "23.03.2018"

