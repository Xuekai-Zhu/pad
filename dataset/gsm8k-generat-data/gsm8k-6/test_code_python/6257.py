def solution():
    # Calculate the weekly use of coffee beans
    morning_use = 3 
    afternoon_use = 3 * 3  # triple the morning use
    evening_use = 2 * 3  # twice the morning use
    weekly_use = (morning_use + afternoon_use + evening_use) * 7  # multiply by 7 days
    result = weekly_use
    return result

print(solution())