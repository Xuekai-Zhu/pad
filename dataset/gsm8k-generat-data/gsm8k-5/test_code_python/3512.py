def solution():
    # Calculate the total number of hours Roy spends on sports activities in school per week
    total_hours_per_week = 2 * 5  # 2 hours per day, 5 days per week

    # Subtract the hours missed due to absences
    hours_missed = 2  # Roy missed 2 days in a week
    hours_spent = total_hours_per_week - (hours_missed * 2)  # 2 hours missed per day

    result = hours_spent
    return result

print(solution())