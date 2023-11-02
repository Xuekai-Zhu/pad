def solution():
    
    jumps_per_minute = 4
    session_time = 10
    sessions_per_day = 2
    days = 5
    total_jumps = jumps_per_minute * session_time * sessions_per_day * days
    result = total_jumps
    return result

print(solution())