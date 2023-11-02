def solution():
    calories_burned_per_day = 2500
    calories_consumed_per_day = 2000
    calories_deficit_per_day = calories_burned_per_day - calories_consumed_per_day
    calories_needed_to_burn_one_pound = 3500  # 1 pound of body fat is equal to 3,500 calories
    pounds_to_burn = 5
    days_to_burn = (calories_needed_to_burn_one_pound * pounds_to_burn) / calories_deficit_per_day
    result = days_to_burn
    return result

print(solution())