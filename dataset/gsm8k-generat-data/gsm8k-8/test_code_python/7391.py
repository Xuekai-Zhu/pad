def solution():
    # Calculate the total cost of washing
    washing_cost = 4 * 2

    # Calculate the total number of minutes for drying
    drying_minutes = 40 * 3

    # Calculate the cost of drying
    drying_cost = (drying_minutes / 10) * 0.25

    # Calculate the total cost of washing and drying
    total_cost = washing_cost + drying_cost
    result = total_cost
    return result

print(solution())