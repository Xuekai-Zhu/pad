def solution():
    # Calculate the time spent on sports activities in school for 5 days
    total_time = 2 * 5  # 2 hours per day, 5 days per week

    # Subtract the hours missed
    time_missed = 2 * 2  # missed 2 days, 2 hours per day
    time_spent = total_time - time_missed
    result = time_spent
    return result

print(solution())