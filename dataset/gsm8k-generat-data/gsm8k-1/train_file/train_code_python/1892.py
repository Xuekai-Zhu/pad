def solution():
    """James gets paid $0.50/mile to drive a truck carrying hazardous waste. He has to pay $4.00/gallon for gas and his truck gets 20 miles per gallon. How much profit does he make from a 600 mile trip?"""
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