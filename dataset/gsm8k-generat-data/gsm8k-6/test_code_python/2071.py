def solution():
    # Calculate the number of push-ups Jackie can do in one minute
    push-ups_per_10_sec = 5  # Jackie can do 5 push-ups in 10 seconds
    push-ups_per_1_sec = push-ups_per_10_sec / 10  # Jackie can do how many push-ups per 1 second
    push-ups_per_1_min = 6 * push-ups_per_1_sec  # Jackie takes two 8-second breaks, so she can exercise for 6 sets of 10 seconds
    result = push-ups_per_1_min
    return result

print(solution())