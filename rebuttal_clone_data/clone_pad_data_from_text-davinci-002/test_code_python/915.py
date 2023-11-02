def solution():
     number_of_bulbs = 40
     watts_per_bulb = 60
     total_watts = number_of_bulbs * watts_per_bulb
     electricity_bill = total_watts * 0.2
     monthly_expenses = electricity_bill * 30
     result = monthly_expenses
     return result

print(solution())