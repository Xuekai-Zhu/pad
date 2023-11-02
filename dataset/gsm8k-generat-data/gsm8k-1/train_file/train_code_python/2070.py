def solution():
    """Jackie can do 5 push-ups in 10 seconds. How many push-ups can she do in one minute if she takes two 8-second breaks?"""
    push_ups_per_10_seconds = 5
    seconds_per_minute = 60
    breaks = 2
    break_time = 8
    total_push_up_time = (seconds_per_minute - (breaks * break_time))
    total_push_ups = (total_push_up_time / 10) * push_ups_per_10_seconds
    result = total_push_ups
    return result

print(solution())