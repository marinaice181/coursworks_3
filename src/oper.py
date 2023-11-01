from _datetime import datetime


class Operation:

    def __init__(self, operation):
        """
        Журнал с данными по операции
        """
        self.operation = operation

    def __repr__(self):
        """
        Возвращает информацию
        """
        return f"{self.operation})"

    def date(self):
        """
        Выводит дату
        """
        operation_date_str = self.operation["date"]
        operation_date = datetime.strptime(operation_date_str, "%Y-%m-%dT%H:%M:%S.%f")
        return operation_date.strftime("%d.%m.%Y")

    def description(self):
        """
        Выводит описание
        """
        return self.operation["description"]

    def account_from(self):
        """
        Выводит данные откуда (может отсутстовать)
        """
        if "from" in self.operation.keys():
            return self.operation["from"]
        else:
            return ""

    def account_to(self):
        """
        Выводит данные куда
        """
        return self.operation["to"]

    def hide_number(self, account):
        if account == "":
            return "Перевод организации"
        else:
            account = account.split(" ")
            account_number = account[-1]
            account.pop(len(account) - 1)
            account_name = " ".join(account)
            if "Счет" in account:
                return f"{account_name} **{account_number[16:20]}"
            else:
                return f"{account_name} {account_number[0:4]} {account_number[4:6]}** **** {account_number[12:16]}"

    def amount(self):
        """Выводит сумму """
        return f'{self.operation["operationAmount"]["amount"]} {self.operation["operationAmount"]["currency"]["name"]}'