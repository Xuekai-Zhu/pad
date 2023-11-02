def solution():
    """Mark collects money for the homeless. He visits 20 households a day for 5 days and half of those households give him a pair of 20s. How much did he collect?"""
    households_visited = 20
    days_visited = 5
    half_households = households_visited / 2
    money_per_pair = 20 * 2
    money_collected = half_households * money_per_pair * days_visited
    result = money_collected
    return result

print(solution())