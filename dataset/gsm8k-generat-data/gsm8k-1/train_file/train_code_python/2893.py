def solution():
    """Ian spent half the money he made on doing online surveys. If he worked 8 hours doing surveys and on average he's able to earn $18 per hour doing surveys, how much money does he have left?"""
    hours_worked = 8
    wage_per_hour = 18
    money_made = hours_worked * wage_per_hour
    money_spent = money_made / 2
    money_left = money_made - money_spent
    result = money_left
    return result

print(solution())