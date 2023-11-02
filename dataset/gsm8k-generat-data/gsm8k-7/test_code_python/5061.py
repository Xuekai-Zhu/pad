def solution():
    hours_per_day = 8
    days_per_week = 5
    math_percentage = 0.25

    # Calculate the total number of hours Ruth spends in school per week
    total_hours = hours_per_day * days_per_week

    # Calculate the total number of hours Ruth spends in math class per week
    math_hours = total_hours * math_percentage

    result = math_hours
    return result

print(solution())