def solution():
    weekdays = 22  # Assuming there are 22 weekdays in a month
    weekends = 8  # Assuming there are 8 weekend days in a month

    # Calculate the amount earned on weekdays
    weekday_income = 600 * weekdays

    # Calculate the amount earned on weekends
    weekend_income = 2 * 600 * weekends  # Twice as much as on weekdays

    # Calculate the total income for the month
    total_income = weekday_income + weekend_income
    result = total_income
    return result

print(solution())