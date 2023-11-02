def solution():
    """Mark collects money for the homeless. He visits 20 households a day for 5 days and half of those households give him a pair of 20s. How much did he collect?"""
    households_visited = 20 * 5
    households_gave = households_visited / 2
    money_collected = households_gave * 2 * 20
    result = money_collected
    return result

print(solution())