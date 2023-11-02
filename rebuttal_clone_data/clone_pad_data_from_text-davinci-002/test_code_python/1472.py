def solution():
     money_borrowed = 100
     monthly_payment = 10
     months_passed = 6
     money_owing = money_borrowed - (monthly_payment * months_passed)
     result = money_owing
     return result

print(solution())