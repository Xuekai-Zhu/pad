def solution():
    """A singer is planning on releasing 3 songs in a month. If he worked on one song for 10 hours a day, and each song took 10 days to be completed, calculate the total number of hours he took to complete the 3 songs."""
    # Define the number of hours per day and days per song
    HOURS_PER_DAY = 10
    DAYS_PER_SONG = 10

    # Calculate the total number of hours
    total_hours = HOURS_PER_DAY * DAYS_PER_SONG * 3

    # Display the total number of hours
    result = total_hours
    return result

print(solution())