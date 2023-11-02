def solution():
    rental_cost = 150
    gas_price = 3.5
    num_gallons = 8
    cost_per_mile = 0.5
    distance = 320

    # Calculate the total cost of gas
    gas_cost = num_gallons * gas_price

    # Calculate the total cost of driving
    driving_cost = distance * cost_per_mile

    # Calculate the total cost of the trip
    total_cost = rental_cost + gas_cost + driving_cost
    result = total_cost
    return result

print(solution())