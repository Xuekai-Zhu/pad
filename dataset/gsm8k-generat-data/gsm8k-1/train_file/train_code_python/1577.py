def solution():
    """Three plastic chairs cost as much as a portable table. Five plastic chairs cost $55. If Manny wants to buy one portable table and two chairs, how much will be left in his $100?"""
    cost_of_5_chairs = 55
    cost_of_1_chair = cost_of_5_chairs / 5
    cost_of_1_table = 3 * cost_of_1_chair
    total_cost = cost_of_1_table + (2 * cost_of_1_chair)
    remaining_money = 100 - total_cost
    result = remaining_money
    return result

print(solution())