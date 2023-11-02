def solution():
    """John can play 200 beats per minute. If he plays 2 hours a day for 3 days how many beats does he play?"""
    # Define the number of minutes in 2 hours
    MINUTES_IN_2_HOURS = 120

    # Define the number of beats John can play in one minute
    BEATS_PER_MINUTE = 200

    # Calculate the total number of beats John can play in 2 hours
    beats_in_2_hours = MINUTES_IN_2_HOURS * BEATS_PER_MINUTE

    # Calculate the total number of beats John plays over 3 days
    total_beats = beats_in_2_hours * 3

    # Display the total number of beats
    result = total_beats
    return result

print(solution())