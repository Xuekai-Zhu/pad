def solution():
    """Jack has 65 pounds of sugar today. Tomorrow he will use 18 pounds of sugar and the following day he will buy 50 more pounds of sugar. How many pounds will he have in the end?"""
    initial_sugar = 65
    used_today = 18
    bought_tomorrow = 50
    remaining_after_tomorrow = initial_sugar - used_today + bought_tomorrow
    result = remaining_after_tomorrow
    return result

print(solution())