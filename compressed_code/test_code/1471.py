def solution():
    
    miles = 600
    pay_per_mile = 0.5
    gas_price_per_gallon = 4.0
    truck_mpg = 20
    gallons_needed = miles / truck_mpg
    gas_cost = gallons_needed * gas_price_per_gallon
    pay_earned = miles * pay_per_mile
    profit = pay_earned - gas_cost
    result = profit
    return result

print(solution())