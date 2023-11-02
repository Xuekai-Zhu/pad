def solution():
    """A singer is planning on releasing 3 songs in a month. If he worked on one song for 10 hours a day, and each song took 10 days to be completed, calculate the total number of hours he took to complete the 3 songs."""
    hours_per_day = 10
    days_per_song = 10
    total_songs = 3
    total_hours = hours_per_day * days_per_song * total_songs
    result = total_hours
    return result

print(solution())