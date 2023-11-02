def solution():
    """Carl types at a speed of 50 words per minute. If he types continuously for 4 hours per day, how many words can he type in 7 days?"""
    # Define the typing speed and hours per day
    typing_speed = 50 # words per minute
    hours_per_day = 4

    # Calculate the number of words typed in one day
    words_per_day = typing_speed * 60 * hours_per_day

    # Calculate the number of words typed in 7 days
    words_in_7_days = words_per_day * 7

    # return the result
    result = words_in_7_days
    return result

print(solution())