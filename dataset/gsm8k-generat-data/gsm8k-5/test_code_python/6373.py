def solution():
    # Calculate the total number of visitors for the first 6 days
    visitors_first_six_days = 100 * 6

    # Calculate the total number of visitors on the last day
    visitors_last_day = visitors_first_six_days * 2

    # Calculate the total number of visitors for the entire week
    total_visitors = visitors_first_six_days + visitors_last_day

    # Calculate the total earnings for the week
    earnings = total_visitors * 0.01
    result = earnings
    return result

print(solution())