def solution():
    """Lucy is listening to her favorite album while jumping rope. She can jump the rope 1 time per second.
    If the album's songs are all 3.5 minutes long and there are 10 songs, how many times will she jump rope?"""
    # Define the duration of a song in seconds
    song_duration = 3.5 * 60

    # Define the total number of songs in the album
    num_songs = 10

    # Calculate the total time for the album
    total_time = song_duration * num_songs

    # Calculate the number of jumps Lucy can do during the album
    num_jumps = total_time

    # Display the number of jumps
    result = num_jumps
    return result

print(solution())