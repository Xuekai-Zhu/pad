def solution():
    """A coffee shop brews 10 coffee cups per hour on a weekday and 120 coffee cups in total over the weekend. 
    If the coffee shop is open 5 hours a day every single day, how many coffee cups are brewed in 1 week?"""
    weekday_cups = 10 * 5 * 5 # 10 cups per hour * 5 hours per day * number of weekdays
    weekend_cups = 120 # given in the problem
    total_cups = weekday_cups + weekend_cups
    result = total_cups
    return result

print(solution())