def solution():
     salary = 80
     monthly_expenses = 42
     monthly_taxes = (salary - monthly_expenses) / 2
     leftover = 18
     taxes_paid = monthly_taxes - leftover
     result = taxes_paid
     return result

print(solution())