def solution():
    """Antonia is trying to improve her health by buying supplements. She has a 7-day pill box she wants to fill. She buys 5 different supplements. 3 of the bottles have 120 pills in them each. 2 of the bottles have 30 pills each. After Antonia has filled her pillbox with one pill of each supplement for 2 weeks, how many pills total does she have left from all 5 bottles?"""
    pill_box_capacity = 7 * 2
    bottle_1 = 120
    bottle_2 = 120
    bottle_3 = 120
    bottle_4 = 30
    bottle_5 = 30
    total_pills = bottle_1 + bottle_2 + bottle_3 + bottle_4 + bottle_5
    pills_per_day = 5
    pills_per_week = pills_per_day * 7
    pills_for_two_weeks = pills_per_week * 2
    total_pills_used = pills_for_two_weeks
    total_pills_left = total_pills - total_pills_used
    result = total_pills_left
    return result

print(solution())