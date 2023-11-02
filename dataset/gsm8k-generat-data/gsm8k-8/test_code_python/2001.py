def solution():
    # Calculate the distance driven in each leg of the trip
    distance_leg1 = 2 * 60
    distance_leg2 = 3 * 50
    total_distance = distance_leg1 + distance_leg2

    # Calculate the total number of gallons of gas used
    total_gallons = total_distance / 30

    # Calculate the total cost of gas
    gas_cost = total_gallons * 2
    result = gas_cost
    return result

print(solution())