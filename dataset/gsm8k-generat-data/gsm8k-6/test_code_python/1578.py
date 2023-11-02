def solution():
    # Calculate the cost of one plastic chair and one portable table
    cost_of_5_chairs = 55
    cost_of_1_chair = cost_of_5_chairs / 5
    cost_of_1_table = 3 * cost_of_1_chair

    # Calculate the total cost of one portable table and two chairs
    total_cost = 1 * cost_of_1_table + 2 * cost_of_1_chair

    # Calculate the amount left from $100
    amount_left = 100 - total_cost
    result = amount_left
    return result

print(solution())