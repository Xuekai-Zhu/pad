def solution():
    """Jackie can do 5 push-ups in 10 seconds. How many push-ups can she do in one minute if she takes two 8-second breaks?"""
    # Define the time per set of push-ups and the number of sets in one minute
    TIME_PER_SET = 10 + 8 + 8
    SETS_PER_MINUTE = 60 // TIME_PER_SET

    # Calculate the total number of push-ups in one minute
    push_ups_per_set = 5
    push_ups_per_minute = push_ups_per_set * SETS_PER_MINUTE

    result = push_ups_per_minute
    return result

print(solution())