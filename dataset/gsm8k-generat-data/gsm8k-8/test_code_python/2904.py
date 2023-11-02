def solution():
    # Calculate the cost of the two parts
    parts_cost = 2 * 20

    # Calculate the cost of labor
    labor_cost = (220 - parts_cost)

    # Convert labor cost from dollars to minutes
    labor_time = labor_cost / 0.5

    # Convert labor time from minutes to hours
    labor_hours = labor_time / 60

    result = labor_hours
    return result

print(solution())