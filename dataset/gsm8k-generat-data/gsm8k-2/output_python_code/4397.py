def solution():
    """An adult panda can eat 138 pounds of bamboo each day. A baby panda can eat 50 pounds of bamboo a day. How many pounds of bamboo will the pandas eat in a week?"""
    adult_daily_eat = 138
    baby_daily_eat = 50
    total_weekly_eat = 7 * (adult_daily_eat + baby_daily_eat)
    result = total_weekly_eat
    return result

print(solution())