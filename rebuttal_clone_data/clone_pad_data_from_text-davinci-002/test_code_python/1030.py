def solution():
    water_cooler = 3
    ounces_per_cup = 6
    total_chairs = 5 * 10
    total_cups = total_chairs
    water_needed = ounces_per_cup * total_cups
    water_left = water_cooler * 128 - water_needed
    result = water_left

Question: Julia consumes 1,500 calories every day.  If she burns 3,500 calories per week through exercise, then how many days will it take her to lose 5 pounds? (There are 3,500 calories in 1 pound.)
Solution: 
def solution():
    calories_needed_to_lose = 5 * 3500
    calories_burned_per_week = 3500
    calories_consumed_per_day = 1500
    calories_deficit_per_day = calories_burned_per_week / 7 - calories_consumed_per_day
    days_needed_to_lose = calories_needed_to_lose / calories_deficit_per_day
    result = days_needed_to_lose
    return result

print(solution())