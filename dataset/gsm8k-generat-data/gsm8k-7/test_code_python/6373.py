def solution():
    num_visitors_per_day = 100
    num_days_without_last_day = 6

    # Calculate the total number of visitors for the first 6 days
    total_visitors_first_six_days = num_visitors_per_day * num_days_without_last_day

    # Calculate the total number of visitors on the last day
    total_visitors_last_day = 2 * total_visitors_first_six_days

    # Calculate the total number of visitors for the week
    total_visitors_for_week = total_visitors_first_six_days + total_visitors_last_day

    # Calculate the total earnings for the week
    total_earnings = total_visitors_for_week * 0.01
    result = total_earnings
    return result

print(solution())