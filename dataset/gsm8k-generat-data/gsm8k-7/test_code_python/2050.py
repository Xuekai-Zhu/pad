def solution():
    first_protest_days = 4
    second_protest_percent_increase = 0.25  # 25% increase

    # Calculate the number of days of the second protest
    second_protest_days = first_protest_days * (1 + second_protest_percent_increase)

    # Calculate the total number of days that John spent protesting
    total_days = first_protest_days + second_protest_days
    result = total_days
    return result

print(solution())