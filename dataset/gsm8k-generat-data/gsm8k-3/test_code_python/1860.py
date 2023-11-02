def solution():
    """A movie that's 1.5 hours long is being replayed 6 times in one movie theater each day. There is a 20-minute advertisement before the start of the movie. How long, in hours, does the movie theater operate each day?"""
    # Define the length of the movie
    MOVIE_LENGTH = 1.5

    # Define the number of times the movie is replayed
    REPLAYS_PER_DAY = 6

    # Define the length of the advertisement
    ADVERTISEMENT_LENGTH = 20 / 60

    # Calculate the total length of each screening, including the advertisement
    screening_length = MOVIE_LENGTH + ADVERTISEMENT_LENGTH

    # Calculate the total length of time the movie theater operates each day
    total_length = screening_length * REPLAYS_PER_DAY

    # Display the total length in hours
    result = total_length
    return result

print(solution())