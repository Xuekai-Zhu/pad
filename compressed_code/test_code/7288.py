def solution():
    
    pay_per_mile = 0.5
    gas_price_per_gallon = 4.0
    miles_per_gallon = 20
    miles_traveled = 600
    gas_used = miles_traveled / miles_per_gallon
    gas_cost = gas_price_per_gallon * gas_used
    total_pay = pay_per_mile * miles_traveled
    profit = total_pay - gas_cost
    result = profit
    return result

print(solution())