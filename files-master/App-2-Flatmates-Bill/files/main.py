class Bill:
    """
    This class represents a bill with the amount to pay for specific time period.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    This class represents flatmate person with number of days he spent in the house.
    It returns how much this person should pay.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        return bill.amount / 2


class PdfReport:
    """
    This class generates pdf file with report about how much each flatmate should pay.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


the_bill = Bill(amount=120, period="March")
flatmate1 = Flatmate(name="Mary", days_in_house=25)
flatmate2 = Flatmate(name="John",days_in_house=20)
print(flatmate1.name, "pays ", flatmate1.pays(bill=the_bill), " , ",
      flatmate2.name, "pays ", flatmate2.pays(bill=the_bill))


