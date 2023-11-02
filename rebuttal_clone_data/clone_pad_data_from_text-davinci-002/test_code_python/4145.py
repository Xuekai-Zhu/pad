def solution():
     car_payment = 400
     tax_percentage = 1/3
     income_after_taxes = car_payment / 0.2
     income_before_taxes = income_after_taxes / (1 - tax_percentage)
     result = income_before_taxes
     return result

print(solution())