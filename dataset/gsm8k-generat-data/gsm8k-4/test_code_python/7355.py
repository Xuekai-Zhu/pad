def solution():
    """Minnie is making a playlist of songs for a party she will be throwing. She wants the playlist to be an hour long. She has added 16 three-minute songs to the playlist. How many four-minute songs does she have to add to make sure the playlist is an hour long?"""
    # Define the length of each song in minutes
    LENGTH_OF_THREE_MIN_SONG = 3
    LENGTH_OF_FOUR_MIN_SONG = 4

    # Define the total length of the playlist in minutes
    TOTAL_PLAYLIST_LENGTH = 60

    # Define the number of three-minute songs already in the playlist
    NUM_THREE_MIN_SONGS = 16

    # Calculate the total length of the three-minute songs in the playlist
    total_length_of_three_min_songs = NUM_THREE_MIN_SONGS * LENGTH_OF_THREE_MIN_SONG

    # Calculate the remaining length of the playlist that needs to be filled with four-minute songs
    remaining_playlist_length = TOTAL_PLAYLIST_LENGTH - total_length_of_three_min_songs

    # Calculate the number of four-minute songs needed to fill the remaining length of the playlist
    num_four_min_songs = remaining_playlist_length // LENGTH_OF_FOUR_MIN_SONG

    # Return the result
    result = num_four_min_songs
    return result

print(solution())