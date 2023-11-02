def solution():
     "
     initial_cost = 1000
     down_payment = initial_cost * 0.2
     additional_down_payment = 20
     total_down_payment = down_payment + additional_down_payment
     monthly_payment = 65
     months_paid = 4
     total_paid = total_down_payment + (monthly_payment * months_paid)
     balance = initial_cost - total_paid
     result = balance
     return result

print(solution())