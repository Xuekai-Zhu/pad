def solution():
    # Calculate the total temperature for the first 3 days
    first_three_days_temp = 40 * 3

    # Calculate the total temperature for Thursday and Friday
    thursday_friday_temp = 80 * 2

    # Calculate the total temperature for the week
    total_week_temp = 60 * 7

    # Calculate the total temperature for the remaining days
    remaining_days_temp = total_week_temp - first_three_days_temp - thursday_friday_temp

    result = remaining_days_temp
    return result

print(solution())