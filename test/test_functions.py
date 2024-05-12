from src.functions import get_executed_operations


def test_get_executed_operations():

    operations = [
        {'state': 'EXECUTED'},
        {'state': 'EXECUTED'},
        {},
        {'state': 'notEXECUTED'},
    ]

    expected_operations = [
        {'state': 'EXECUTED'},
        {'state': 'EXECUTED'},
    ]

    assert get_executed_operations(operations) == expected_operations
    assert get_executed_operations([]) == []
