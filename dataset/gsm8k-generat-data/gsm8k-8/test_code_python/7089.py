def solution():
    # Calculate the cost for Monday's trip
    monday_cost = 150 + (620 * 0.5)

    # Calculate the cost for Thursday's trip
    thursday_cost = 150 + (744 * 0.5)

    # Calculate the total cost
    total_cost = monday_cost + thursday_cost
    result = total_cost
    return result

print(solution())