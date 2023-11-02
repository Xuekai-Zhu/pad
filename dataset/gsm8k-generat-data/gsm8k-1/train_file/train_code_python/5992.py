def solution():
    """John wants to lose weight. He eats 1800 calories a day and burns 2300 a day. If he needs to burn 4000 calories to lose 1 pound how many days will it take to lose 10 pounds?"""
    calories_eaten_per_day = 1800
    calories_burned_per_day = 2300
    calories_needed_to_lose_1lb = 4000
    calories_deficit_per_day = calories_burned_per_day - calories_eaten_per_day
    pounds_lost_per_day = calories_deficit_per_day / calories_needed_to_lose_1lb
    days_to_lose_10lbs = 10 / pounds_lost_per_day
    result = days_to_lose_10lbs
    return result

print(solution())