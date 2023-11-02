def solution():
    hours_per_day = 5
    num_days_first_month = 30
    num_days_second_month = 12

    # Calculate the total number of hours trained in the first month
    total_hours_first_month = hours_per_day * num_days_first_month

    # Calculate the total number of hours trained in the second month
    total_hours_second_month = hours_per_day * num_days_second_month

    # Calculate the total number of hours trained in both months
    total_hours = total_hours_first_month + total_hours_second_month
    result = total_hours
    return result

print(solution())