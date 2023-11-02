def solution():
    # Calculate the cost of one plastic chair
    chair_cost = 55 / 5

    # Calculate the cost of one portable table
    table_cost = 3 * chair_cost

    # Calculate the total cost of one table and two chairs
    total_cost = table_cost + (2 * chair_cost)

    # Calculate the amount left in Manny's $100 after the purchase
    left_amount = 100 - total_cost
    result = left_amount
    return result

print(solution())