def solution():
    current_time = 30  # Chris can hold his breath for 30 seconds after 3 days
    extra_time_per_day = 10  # Chris can hold his breath for 10 extra seconds each day
    remaining_time = 90 - current_time  # Chris needs to hold his breath for 90 seconds in total
    required_days = remaining_time / extra_time_per_day

    # Add the previous 3 days to get the total number of days
    total_days = required_days + 3
    result = total_days
    return result

print(solution())