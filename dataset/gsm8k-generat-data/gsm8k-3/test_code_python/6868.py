def solution():
    """Tim spends 1 hour a day meditating.  He spends twice as much time reading.  How much time a week does he spend reading?"""
    # Define the time Tim spends meditating and reading each day
    MEDITATION_TIME = 1
    READING_TIME = 2 * MEDITATION_TIME

    # Calculate the total time Tim spends reading in a week
    total_reading_time = READING_TIME * 7

    # Display the total time Tim spends reading in a week
    result = total_reading_time
    return result

print(solution())