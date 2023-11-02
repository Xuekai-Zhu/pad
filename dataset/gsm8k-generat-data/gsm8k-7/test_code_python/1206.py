def solution():
    jumps_per_minute = 4
    minutes_per_session = 10
    sessions_per_day = 2
    days = 5

    # Calculate the total number of jumps per session
    total_jumps_per_session = jumps_per_minute * minutes_per_session

    # Calculate the total number of jumps per day
    total_jumps_per_day = total_jumps_per_session * sessions_per_day

    # Calculate the total number of jumps in 5 days
    total_jumps_in_5_days = total_jumps_per_day * days
    result = total_jumps_in_5_days
    return result

print(solution())