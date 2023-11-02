def solution():
    rate_per_mile = 0.5  # James gets paid $0.50 per mile
    gas_cost_per_gallon = 4  # James pays $4.00 per gallon for gas
    truck_miles_per_gallon = 20  # James's truck gets 20 miles per gallon
    distance = 600  # James is driving 600 miles

    # Calculate the gas cost for the trip
    gas_cost = (distance / truck_miles_per_gallon) * gas_cost_per_gallon

    # Calculate James's earnings for the trip
    earnings = distance * rate_per_mile

    # Calculate James's profit for the trip
    profit = earnings - gas_cost
    result = profit
    return result

print(solution())