def solution():
    """James spends 30 minutes twice a day on meditation.  How many hours a week does he spend meditating?"""
    # Define the amount of time James spends per meditation session
    MEDITATION_TIME = 30 # in minutes

    # Define the number of meditation sessions James does per day
    SESSIONS_PER_DAY = 2

    # Calculate the total time James spends meditating per week
    total_time = MEDITATION_TIME * SESSIONS_PER_DAY * 7 / 60 # convert to hours

    # Display the total time James spends meditating per week
    result = total_time
    return result

print(solution())