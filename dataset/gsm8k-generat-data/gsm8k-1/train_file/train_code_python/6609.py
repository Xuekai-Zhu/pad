def solution():
    """In a week, Mortdecai collects 8 dozen eggs every Tuesday and Thursday, and he delivers 3 dozen eggs to the market and 5 dozen eggs to the mall. He then uses 4 dozen eggs to make a pie every Saturday. Mortdecai donates the remaining eggs to the charity by Sunday. How many eggs does he donate to the charity?"""
    eggs_collected = 8*2  # 8 dozen eggs collected twice a week
    eggs_delivered = 3*2 + 5*2  # 3 dozen eggs to market + 5 dozen eggs to mall collected twice a week
    eggs_used = 4  # 4 dozen eggs used to make a pie every Saturday
    eggs_remaining = eggs_collected - eggs_delivered - eggs_used
    eggs_donated = eggs_remaining * 12  # convert dozen to single eggs
    result = eggs_donated
    return result

print(solution())