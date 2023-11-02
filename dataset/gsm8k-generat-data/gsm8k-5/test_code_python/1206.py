def solution():
    jumps_per_minute = 4  # Spencer jumps rope 4 times per minute
    minutes_per_session = 10  # Spencer jumps rope for 10 minutes each session
    sessions_per_day = 2  # Spencer does 2 sessions each day
    days = 5  # Spencer wants to know how many jumps he will do in 5 days

    # Calculate the total number of jumps Spencer will do in 5 days
    total_jumps = jumps_per_minute * minutes_per_session * sessions_per_day * days
    result = total_jumps
    return result

print(solution())