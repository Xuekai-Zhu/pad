def solution():
    # Number of push-ups Jackie can do in 10 seconds
    push_ups_per_10_sec = 5

    # Total number of seconds in a minute
    sec_in_min = 60

    # Total time taken for push-ups and breaks
    total_time = 3*8 + 50*10  # Two 8-sec breaks and 50 sets of 10 seconds for push-ups

    # Number of push-ups Jackie can do in one minute
    push_ups_per_min = (total_time / 10) * push_ups_per_10_sec
    
    result = push_ups_per_min
    return result

print(solution())