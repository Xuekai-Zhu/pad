def solution():
    # Calculate the number of glasses of water Mary should drink per day
    goal_liters = 1.5
    goal_milliliters = goal_liters * 1000
    glass_size = 250
    glasses_per_day = goal_milliliters / glass_size
    result = glasses_per_day
    return result

print(solution())