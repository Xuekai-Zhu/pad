def solution():
    daily_flies = 2 # number of flies the frog eats every day
    morning_flies = 5 # number of flies caught in the morning
    afternoon_flies = 6 - 1 # number of flies caught in the afternoon, minus the one that escaped
    total_flies_per_day = morning_flies + afternoon_flies # total number of flies caught per day
    days_per_week = 7 # number of days in a week
    
    # Calculate the total number of flies caught in a week
    total_flies_per_week = total_flies_per_day * days_per_week
    
    # Calculate the total number of flies the frog will eat in a week
    total_frog_food_per_week = daily_flies * days_per_week
    
    # Calculate the number of additional flies Betty needs to gather for the whole week's food for her frog
    additional_flies_needed = total_frog_food_per_week - total_flies_per_week
    
    result = additional_flies_needed
    return result

print(solution())