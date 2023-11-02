def solution():
    """James gets paid $0.50/mile to drive a truck carrying hazardous waste. He has to pay $4.00/gallon for gas and his truck gets 20 miles per gallon. How much profit does he make from a 600 mile trip?"""
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