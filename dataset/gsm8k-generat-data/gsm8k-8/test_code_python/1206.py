def solution():
    jumps_per_minute = 4
    session_duration = 10
    sessions_per_day = 2
    days = 5

    jumps_per_session = jumps_per_minute * session_duration
    total_jumps_per_day = jumps_per_session * sessions_per_day
    total_jumps_in_5_days = total_jumps_per_day * days
    result = total_jumps_in_5_days
    return result

print(solution())