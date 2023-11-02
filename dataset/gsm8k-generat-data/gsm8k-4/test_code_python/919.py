def solution():
    """Aisha enjoys listening to music on her mp3 player. She starts with 500 songs on her mp3 player, then adds another 500 the week after that. She realizes her mp3 player has a large capacity for storing songs so she adds twice the amount she already had on her mp3 player. After a while, though, she decides that she doesn't like 50 of the songs and removes them. How many songs are on Aisha's mp3 player now?"""
    # Define the initial number of songs
    songs = 500

    # Add another 500 songs
    songs += 500

    # Add twice the initial number of songs
    songs += 2 * 500

    # Remove 50 songs
    songs -= 50

    result = songs
    return result

print(solution())