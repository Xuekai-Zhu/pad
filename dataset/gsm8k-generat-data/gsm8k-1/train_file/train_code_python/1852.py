def solution():
    """How many shirts should Shenny pack for her next vacation if she's planning to use the same shirt when departing on Monday and returning on Sunday and two different shirts each other day?"""
    days_other_than_mon_sun = 5
    shirts_per_day = 2
    total_shirts = 1 + (shirts_per_day * days_other_than_mon_sun) + 1
    result = total_shirts
    return result

print(solution())