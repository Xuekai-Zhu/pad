def solution():
    """Stan makes a playlist for the next time he goes running. He has 10 3-minute songs and 15 2-minute songs on his playlist. His entire run takes 100 minutes. If Stan wants a playlist to cover his entire run, how many more minutes of songs will he need in his playlist?"""
    # Define the length of each song in minutes
    SONG_3MIN = 3
    SONG_2MIN = 2

    # Define the number of songs of each length on the playlist
    num_songs_3min = 10
    num_songs_2min = 15

    # Calculate the total length of the songs currently on the playlist
    total_length = num_songs_3min * SONG_3MIN + num_songs_2min * SONG_2MIN

    # Calculate the remaining time needed to cover the entire run
    remaining_time = 100 - total_length

    # Display the remaining time needed
    result = remaining_time
    return result

print(solution())