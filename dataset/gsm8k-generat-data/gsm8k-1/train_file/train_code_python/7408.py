def solution():
    """Bill is hoarding toilet paper in fear of another pandemic. Bill goes to the bathroom three times a day and uses 5 squares of toilet paper each time. If Bill has 1000 rolls of toilet paper and each roll has 300 squares of toilet paper, how many days will his toilet paper supply last?"""
    rolls_of_tp = 1000
    squares_per_roll = 300
    squares_used_per_day = 3 * 5
    days_of_supply = (rolls_of_tp * squares_per_roll) / squares_used_per_day
    result = days_of_supply
    return result

print(solution())