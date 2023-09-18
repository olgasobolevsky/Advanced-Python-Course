class Bill:
    """
    This class represents a bill with the amount to pay for specific time period.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Flatmate person with number of days he spent in the house.
    It returns how much this person should pay for his stay in the house.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, co_flatmate):
        weight = self.days_in_house / (self.days_in_house + co_flatmate.days_in_house)
        return bill.amount * weight