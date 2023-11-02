def solution():
    """Jamie's father gained 5 pounds over the holidays that he wants to lose so his pants will not be as snug. He asks Jamie to help him keep track of his calories. Jamie's father burns 2,500 calories of fat a day by doing light exercise. There are 3,500 calories in a pound of body fat. How many days will it take for Jamie's father to burn off 5 pounds if he does light exercise and sticks to eating 2000 calories a day?"""
    pounds_to_lose = 5
    calories_per_pound = 3500
    total_calories_to_lose = pounds_to_lose * calories_per_pound
    daily_calorie_deficit = 500
    calories_burned_per_day = 2500
    calories_consumed_per_day = 2000
    calories_deficit_per_day = calories_burned_per_day - calories_consumed_per_day
    days_to_lose_weight = total_calories_to_lose/(calories_deficit_per_day)
    result = days_to_lose_weight
    return result

print(solution())