def solution():
    """A movie that's 1.5 hours long is being replayed 6 times in one movie theater each day. There is a 20-minute advertisement before the start of the movie. How long, in hours, does the movie theater operate each day?"""
    # Define the length of the movie and the number of times it is replayed
    movie_length = 1.5
    replay_times = 6

    # Define the length of the advertisement
    ad_length = 20/60

    # Calculate the total length of one screening including the advertisement
    total_length = movie_length + ad_length

    # Calculate the total length of all screenings
    total_screening_length = total_length * replay_times

    # Convert the total length to hours
    total_hours = total_screening_length / 60

    result = total_hours
    return result

print(solution())