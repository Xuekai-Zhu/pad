def solution():
    jumps_per_minute = 4
    minutes_per_session = 10
    sessions_per_day = 2
    days = 5
    total_jumps = jumps_per_minute * minutes_per_session * sessions_per_day * days
    result = total_jumps
    return result

print(solution())