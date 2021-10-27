from enum import Enum

class TimeFrameUnit(Enum):
    Minute = "Min"
    Hour = "Hour"
    Day = "Day"

class TimeFrame:
    """Represents a unit of data resolution"""
    def __init__(self, amount: int, unit: TimeFrameUnit):
        self.validate(amount, unit)
        self.__amount = amount
        self.__unit = unit

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value: int):
        self.validate(value, self.__unit)
        self.__amount = value

    @property
    def unit(self) -> TimeFrameUnit:
        return self.__unit

    @unit.setter
    def unit(self, value: TimeFrameUnit):
        self.validate(self.__amount, value)
        self.__unit = value

    # using "value" field for backwards compatibility
    @property
    def value(self):
        return f"{self.__amount}{self.__unit.value}"

    def __str__(self):
        return self.value

    @staticmethod
    def validate(amount: int, unit: TimeFrameUnit):
        if amount <= 0:
            raise "Amount must be a positive integer value."

        if unit == TimeFrameUnit.Minute and amount > 59:
            raise "Second or Minute units can only be used " + \
                "with amounts between 1-59."

        if unit == TimeFrameUnit.Hour and amount > 23:
            raise "Hour units can only be used with amounts 1-23"