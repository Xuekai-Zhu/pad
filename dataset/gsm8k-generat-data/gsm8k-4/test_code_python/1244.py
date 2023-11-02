def solution():
    """A singer is planning on releasing 3 songs in a month. If he worked on one song for 10 hours a day, and each song took 10 days to be completed, calculate the total number of hours he took to complete the 3 songs."""
    # Define the number of hours spent on each song per day and the number of days to complete a song
    HOURS_PER_DAY = 10
    DAYS_PER_SONG = 10

    # Calculate the total number of hours spent on one song
    hours_per_song = HOURS_PER_DAY * DAYS_PER_SONG

    # Calculate the total number of hours spent on all three songs
    total_hours = hours_per_song * 3

    result = total_hours
    return result

print(solution())