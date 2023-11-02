def solution():
    # Calculate the cost of one plastic chair
    chair_cost = 55 / 5  # Five plastic chairs cost $55

    # Calculate the cost of one portable table
    table_cost = 3 * chair_cost  # Three plastic chairs cost as much as a portable table

    # Calculate the total cost of one portable table and two chairs
    total_cost = table_cost + (2 * chair_cost)

    # Calculate how much will be left in Manny's $100
    left_over = 100 - total_cost
    result = left_over
    return result

print(solution())