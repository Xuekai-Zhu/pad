def solution():
    # Calculate the volume of concrete needed for the 3 slabs
    volume = 100 * 100 * 0.5  # volume in cubic feet

    # Calculate the weight of concrete needed for the 3 slabs
    weight = volume * 150  # weight in pounds

    # Calculate the cost of the concrete needed for the 3 slabs
    cost = weight * 0.02  # cost in dollars

    # Round the cost to 2 decimal places
    rounded_cost = round(cost, 2)

    result = rounded_cost
    return result

print(solution())