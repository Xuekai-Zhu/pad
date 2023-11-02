def solution():
    """Bart makes a mixtape. The first side has 6 songs. The second side has 4 songs. Each song is 4 minutes. How long is the total tape?"""
    # Define the number of songs and duration of each song
    songs_per_side = 4
    song_duration = 4

    # Calculate the duration of the first side
    first_side_duration = songs_per_side * song_duration * 6

    # Calculate the duration of the second side
    second_side_duration = songs_per_side * song_duration * 4

    # Calculate the total duration of the tape
    total_duration = first_side_duration + second_side_duration

    # return the result in minutes
    result = total_duration
    return result

print(solution())