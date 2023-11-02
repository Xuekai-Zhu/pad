def solution():
    pay_per_mile = 0.5
    gas_cost_per_gallon = 4.0
    miles_per_gallon = 20
    miles = 600

    # Calculate total earnings from the trip
    earnings = pay_per_mile * miles

    # Calculate total cost of gas for the trip
    gas_cost = (miles / miles_per_gallon) * gas_cost_per_gallon

    # Calculate total profit
    profit = earnings - gas_cost
    result = profit
    return result

print(solution())