def solution():
    """Jackie can do 5 push-ups in 10 seconds. How many push-ups can she do in one minute if she takes two 8-second breaks?"""
    push_ups_in_10_sec = 5
    break_time = 2 * 8
    full_minute_time = 60 - break_time
    push_ups_per_minute = (push_ups_in_10_sec * 6) * full_minute_time
    result = push_ups_per_minute
    return result

print(solution())