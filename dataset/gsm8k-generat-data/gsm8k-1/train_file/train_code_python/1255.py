def solution():
    """Conor can chop 12 eggplants, 9 carrots, and 8 potatoes in a day. If he works 4 times a week, how many vegetables can he chop?"""
    eggplants_per_day = 12
    carrots_per_day = 9
    potatoes_per_day = 8
    days_per_week = 4
    total_vegetables = (eggplants_per_day + carrots_per_day + potatoes_per_day) * days_per_week
    result = total_vegetables
    return result

print(solution())