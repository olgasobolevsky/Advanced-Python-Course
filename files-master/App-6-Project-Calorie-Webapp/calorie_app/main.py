
from calculators import CalorieCalculator
from temperature import Temperature


temp = Temperature(country='israel', city='tel-aviv')
calc = CalorieCalculator(weight=53, height=162, age=45, temperature=29)
print(calc.calculate())
