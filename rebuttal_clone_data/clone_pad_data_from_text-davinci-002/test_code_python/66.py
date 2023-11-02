def solution():
     """"Tara has been planning to buy a laptop which costs $1000. A computer shop accepts payment in installments of $65 per month provided that a 20% down payment is made. If Tara wants to pay an additional $20 for the down payment, how much will her balance be after paying for 4 months?"""
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