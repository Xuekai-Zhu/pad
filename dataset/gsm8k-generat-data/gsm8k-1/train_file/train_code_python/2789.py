def solution():
    """Four small panda bears and five bigger panda bears eat 25 pounds and 40 pounds of fresh bamboo sprouts every day, respectively. How many pounds of bamboo do the 9 pandas eat in a week?"""
    small_bears_per_day = 4
    big_bears_per_day = 5
    small_bear_food_per_day = 25
    big_bear_food_per_day = 40
    total_bears_per_day = small_bears_per_day + big_bears_per_day
    total_food_per_day = small_bears_per_day * small_bear_food_per_day + big_bears_per_day * big_bear_food_per_day
    total_food_per_week = total_food_per_day * 7
    result = total_food_per_week
    return result

print(solution())