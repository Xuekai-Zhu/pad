def solution():
    """Hansel has a created album on Spotify that contains 25 songs and each song is 3 minutes long.
       If she adds 10 more songs to the album with the same duration, how many minutes will it take her to finish all the songs in the album?"""
    
    # Define the number of songs and the duration per song
    num_songs = 25 + 10
    song_length = 3

    # Calculate the total duration of all the songs in the album
    total_duration = num_songs * song_length

    # Display the total duration in minutes
    result = total_duration
    return result

print(solution())