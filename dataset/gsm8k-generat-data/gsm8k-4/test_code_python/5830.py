def solution():
    """Hansel has a created album on Spotify that contains 25 songs and each song is 3 minutes long. If she adds 10 more songs to the album with the same duration, how many minutes will it take her to finish all the songs in the album?"""
    # Define the number of songs and the duration of each song
    num_songs = 25
    song_duration = 3

    # Calculate the total duration of the initial album
    initial_duration = num_songs * song_duration

    # Calculate the total duration of the expanded album
    expanded_duration = (num_songs + 10) * song_duration

    # Calculate the total duration of all the songs in the album
    total_duration = initial_duration + expanded_duration

    # return the result in minutes
    result = total_duration
    return result

print(solution())