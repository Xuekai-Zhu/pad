def solution():
    # Calculate the cost of renting a car for a year
    rent_cost = 20 * 12  # $20 per month, 12 months

    # Calculate the cost of buying a new car for a year
    new_car_cost = 30 * 12  # $30 per month, 12 months

    # Calculate the difference in cost between renting and buying a new car
    cost_difference = new_car_cost - rent_cost
    result = cost_difference
    return result

print(solution())