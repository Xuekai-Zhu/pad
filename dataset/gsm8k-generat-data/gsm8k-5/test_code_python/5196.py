def solution():
    daily_reading_time = 2  # Mark reads books for 2 hours each day
    weekly_increase = 4  # Mark wants to increase his weekly reading time by 4 hours

    # Calculate the new weekly reading time
    new_weekly_reading_time = (daily_reading_time * 7) + weekly_increase

    result = new_weekly_reading_time
    return result

print(solution())