def solution():
     initial_pay = 650
     tax_rate = 10
     tax_amount = initial_pay * (tax_rate / 100)
     take_home_pay = initial_pay - tax_amount
     result = take_home_pay
     return result

print(solution())