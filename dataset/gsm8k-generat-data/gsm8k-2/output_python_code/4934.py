def solution():
    """Jamie's father gained 5 pounds over the holidays that he wants to lose so his pants will not be as snug. He asks Jamie to help him keep track of his calories. Jamie's father burns 2,500 calories of fat a day by doing light exercise. There are 3,500 calories in a pound of body fat. How many days will it take for Jamie's father to burn off 5 pounds if he does light exercise and sticks to eating 2000 calories a day?"""
    pounds_to_burn = 5
    calories_in_pound = 3500
    deficit_calories_per_day = 500 # 2500 (burned) - 2000 (eaten)
    total_deficit_calories = pounds_to_burn * calories_in_pound
    total_days = total_deficit_calories / deficit_calories_per_day
    result = total_days 
    return result

print(solution())