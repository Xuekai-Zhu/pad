def solution():
    """Three plastic chairs cost as much as a portable table. Five plastic chairs cost $55. If Manny wants to buy one portable table and two chairs, how much will be left in his $100?"""
  
    # Determine the cost of one plastic chair
    chair_cost = 55 / 5  # 5 plastic chairs cost $55, so one plastic chair costs $11

    # Determine the cost of one portable table
    table_cost = chair_cost * 3  # Three plastic chairs cost as much as a portable table

    # Determine the total cost of one portable table and two chairs
    total_cost = table_cost + (chair_cost * 2)

    # Determine how much money Manny will have left after making the purchase
    money_left = 100 - total_cost

    result = money_left
    return result

print(solution())