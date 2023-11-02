def solution():
    """In a week, Mortdecai collects 8 dozen eggs every Tuesday and Thursday, and he delivers 3 dozen eggs to the market and 5 dozen eggs to the mall. He then uses 4 dozen eggs to make a pie every Saturday. Mortdecai donates the remaining eggs to the charity by Sunday. How many eggs does he donate to the charity?"""
    eggs_collected_per_week = 8 * 2  # collected on Tuesdays and Thursdays
    eggs_delivered_to_market = 3 * 2  # delivered on Tuesdays and Thursdays
    eggs_delivered_to_mall = 5 * 2  # delivered on Tuesdays and Thursdays
    eggs_used_for_pies = 4
    total_eggs_used = eggs_delivered_to_market + eggs_delivered_to_mall + eggs_used_for_pies
    remaining_eggs = eggs_collected_per_week - total_eggs_used
    eggs_donated_to_charity = remaining_eggs
    result = eggs_donated_to_charity
    return result

print(solution())