def solution():
    """An adult panda can eat 138 pounds of bamboo each day. A baby panda can eat 50 pounds of bamboo a day. How many pounds of bamboo will the pandas eat in a week?"""
    adult_daily = 138
    baby_daily = 50
    days_per_week = 7
    total_bamboo = (adult_daily + baby_daily) * days_per_week
    result = total_bamboo
    return result

print(solution())