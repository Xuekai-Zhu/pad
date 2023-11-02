def solution():
    """Three plastic chairs cost as much as a portable table. Five plastic chairs cost $55. If Manny wants to buy one portable table and two chairs, how much will be left in his $100?"""
    # Calculate the cost of one plastic chair
    chair_cost = 55/5

    # Calculate the cost of one portable table
    table_cost = chair_cost * 3

    # Calculate the total cost of one portable table and two plastic chairs
    total_cost = table_cost + (chair_cost * 2)

    # Calculate the amount left in Manny's $100 after the purchase
    remaining_amount = 100 - total_cost

    # return the result
    result = remaining_amount
    return result

print(solution())