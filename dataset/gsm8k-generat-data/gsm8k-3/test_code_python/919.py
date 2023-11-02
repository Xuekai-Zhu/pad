def solution():
    """Aisha enjoys listening to music on her mp3 player. She starts with 500 songs on her mp3 player, then adds another 500 the week after that. She realizes her mp3 player has a large capacity for storing songs so she adds twice the amount she already had on her mp3 player. After a while, though, she decides that she doesn't like 50 of the songs and removes them. How many songs are on Aisha's mp3 player now?"""
    # Define the initial number of songs on Aisha's mp3 player
    initial_songs = 500

    # Add another 500 songs
    songs_after_first_week = initial_songs + 500

    # Add twice the initial amount of songs
    songs_after_second_week = songs_after_first_week + (2 * initial_songs)

    # Remove 50 songs
    songs_after_removal = songs_after_second_week - 50

    # Display the total number of songs on Aisha's mp3 player now
    result = songs_after_removal
    return result

print(solution())