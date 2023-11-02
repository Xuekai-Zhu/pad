def solution():
    """Bill is hoarding toilet paper in fear of another pandemic. Bill goes to the bathroom three times a day and uses 5 squares of toilet paper each time. If Bill has 1000 rolls of toilet paper and each roll has 300 squares of toilet paper, how many days will his toilet paper supply last?"""
    rolls_of_toilet_paper = 1000
    squares_per_roll = 300
    daily_use = 3 * 5
    total_squares_used_per_day = daily_use
    total_squares = rolls_of_toilet_paper * squares_per_roll
    days_supply = total_squares / total_squares_used_per_day
    result = days_supply
    return result

print(solution())