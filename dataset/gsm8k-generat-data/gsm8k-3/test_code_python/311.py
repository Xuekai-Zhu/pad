def solution():
    """Carl types at a speed of 50 words per minute. If he types continuously for 4 hours per day, how many words can he type in 7 days?"""
    # Define Carl's typing speed and hours worked per day
    WORDS_PER_MINUTE = 50
    HOURS_PER_DAY = 4

    # Calculate the number of words Carl can type in one day
    words_per_day = WORDS_PER_MINUTE * 60 * HOURS_PER_DAY

    # Calculate the number of words Carl can type in 7 days
    words_per_week = words_per_day * 7

    # Display the total number of words Carl can type in 7 days
    result = words_per_week
    return result

print(solution())