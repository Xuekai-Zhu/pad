def solution():
     miles_driven = 600
     gas_price = 4.00
     gas_consumed = miles_driven / 20
     gas_cost = gas_price * gas_consumed
     pay_per_mile = 0.50
     pay = pay_per_mile * miles_driven
     profit = pay - gas_cost
     result = profit
     
     return result

print(solution())