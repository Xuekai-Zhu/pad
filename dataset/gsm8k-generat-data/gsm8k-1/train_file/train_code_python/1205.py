def solution():
    """When Spencer jumps rope, he jumps 4 times per minute. He jumps for 10 minutes each session and does 2 sessions each day. How many jumps will Spencer do in 5 days?"""
    jumps_per_minute = 4
    minutes_per_session = 10
    sessions_per_day = 2
    days = 5
    total_jumps = jumps_per_minute * minutes_per_session * sessions_per_day * days
    result = total_jumps
    return result

print(solution())