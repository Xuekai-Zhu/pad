def solution():
    """Minnie is making a playlist of songs for a party she will be throwing. She wants the playlist to be an hour long. She has added 16 three-minute songs to the playlist. How many four-minute songs does she have to add to make sure the playlist is an hour long?"""
    # Define the length of each song in minutes
    THREE_MINUTES = 3
    FOUR_MINUTES = 4

    # Define the length of the playlist in minutes
    playlist_length = 60

    # Calculate the total length of the 16 three-minute songs
    total_length_of_three_min_songs = THREE_MINUTES * 16

    # Calculate the remaining time needed for the playlist to be one hour long
    remaining_time = playlist_length - total_length_of_three_min_songs

    # Calculate the number of four-minute songs needed to fill the remaining time
    number_of_four_min_songs = remaining_time // FOUR_MINUTES

    # Display the number of four-minute songs needed
    result = number_of_four_min_songs
    return result

print(solution())