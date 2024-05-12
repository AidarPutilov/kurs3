from datetime import datetime


class Operation:
    """ Класс, описывающий операцию """

    def __init__(
            self,
            pk: int,
            state: str,
            date_time: str,
            amount: str,
            currency: str,
            description: str,
            from_: str = None,
            to: str = None
    ):
        self.pk = pk
        self.state = state
        self.date_time = self.get_date_time(date_time)
        self.date = self.get_date_str()
        self.amount = amount
        self.currency = currency
        self.description = description
        self.from_type = self.convert_pay('type', from_) if from_ is not None else ''
        self.from_number = self.convert_pay('number', from_) if from_ is not None else ''
        self.to_type = self.convert_pay('type', to) if to is not None else ''
        self.to_number = self.convert_pay('number', to) if to is not None else ''
        self.from_number_encript = self.get_encript_number(from_) if from_ is not None else ''
        self.to_number_encript = self.get_encript_number(to) if to is not None else ''

    def convert_pay(self, var: str, pay: str) -> str:
        """ Возвращает вид (var='type') или номер (var='number') счёта/карты """
        if var == 'type':
            if pay.startswith('Счет'):
                return pay.split()[0]
            else:
                return ' '.join(pay.split()[:-1])
        elif var == 'number':
            return pay.split()[-1]

    def get_encript_number(self, pay: str) -> str:
        """ Возвращает номер счёта/карты в защищённом виде """
        string = pay.split()[-1]
        if pay.startswith('Счет'):
            return 2 * '*' + string[-4:]
        else:
            card_number = string[:6] + (len(string[6:-4]) * '*') + string[-4:]
            card_list = [card_number[i:i + 4] for i in range(0, len(card_number), 4)]
            return ' '.join(card_list)

    def get_date_time(self, date_time: str):
        """ Возвращает дату/время в универсальном формате """
        return datetime.fromisoformat(date_time)

    def get_date_str(self) -> str:
        """ Возвращает дату в виде 01.01.2000 """
        return self.date_time.strftime('%d.%m.%Y')

    def get_status(self):
        """ Возвращает статус операции """
        string = f'{self.date} {self.description}\n' \
                  f'{self.from_type} {self.from_number_encript} -> '\
                  f'{self.to_type} {self.to_number_encript}\n' \
                  f'{self.amount} {self.currency}\n'
        return string

    def __lt__(self, other):
        return self.date_time < other.date_time

    def __gt__(self, other):
        return self.date_time > other.date_time

    def __str__(self):
        return f'Operation(pk={self.pk}, state={self.state}, date={self.date}, amount={self.amount}), ' \
                f'currency={self.currency}, description={self.description}, ' \
                f'from={self.from_type} {self.from_number}, to={self.to_type} {self.to_number})'
