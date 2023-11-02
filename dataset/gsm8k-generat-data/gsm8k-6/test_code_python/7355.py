def solution():
    # Calculate the total length of the 16 three-minute songs
    length_of_16_songs = 16 * 3  # each song is 3 minutes long

    # Calculate the remaining time needed for the playlist to be an hour long
    remaining_time = 60 - length_of_16_songs

    # Calculate the number of four-minute songs needed to fill the remaining time
    number_of_four_minute_songs = remaining_time // 4 

    result = number_of_four_minute_songs
    return result

print(solution())