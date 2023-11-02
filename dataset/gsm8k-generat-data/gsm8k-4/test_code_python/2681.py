def solution():
    """Jonathan eats 2500 calories every day except for Saturday, when he consumes an extra 1000 calories. He burns 3000 calories every day. What is his weekly caloric deficit?"""
    
    # Define the daily caloric intake and caloric burn
    daily_calories_intake = 2500
    saturday_calories_intake = 3500
    daily_calories_burn = 3000
    
    # Calculate the daily caloric deficit
    daily_caloric_deficit = daily_calories_intake - daily_calories_burn
    
    # Calculate the weekly caloric deficit
    weekly_caloric_deficit = (6 * daily_caloric_deficit) + (1 * (saturday_calories_intake - daily_calories_burn))
    
    result = weekly_caloric_deficit
    return result

print(solution())