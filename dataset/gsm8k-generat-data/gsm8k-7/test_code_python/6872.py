def solution():
    daily_goal = 1.5 # liters
    glass_size = 250 # mL

    # Convert daily goal to mL
    daily_goal_mL = daily_goal * 1000

    # Calculate the number of glasses Mary should drink per day
    num_glasses = daily_goal_mL / glass_size

    result = num_glasses
    return result

print(solution())