def solution():
    """Gabe has three songs on his playlist. “The Best Day” is 3 minutes, “Raise the Roof” is 2 minutes, and “Rap Battle” is 3 minutes. How many times can Gabe listen to his entire playlist on the 40-minute ride to his wrestling match?"""
    # Define the length of each song in minutes
    SONG_1_LENGTH = 3
    SONG_2_LENGTH = 2
    SONG_3_LENGTH = 3

    # Define the total length of the playlist in minutes
    PLAYLIST_LENGTH = SONG_1_LENGTH + SONG_2_LENGTH + SONG_3_LENGTH

    # Calculate how many times Gabe can listen to the entire playlist during his 40-minute ride
    num_plays = 40 // PLAYLIST_LENGTH

    # Display the number of times Gabe can listen to his playlist
    result = num_plays
    return result

print(solution())