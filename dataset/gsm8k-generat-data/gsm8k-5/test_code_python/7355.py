def solution():
    total_length = 60  # Minnie wants the playlist to be an hour long
    added_songs_length = 16 * 3  # Minnie has added 16 three-minute songs

    # Calculate the remaining length that needs to be filled with four-minute songs
    remaining_length = total_length - added_songs_length
    # Calculate the number of four-minute songs needed to fill the remaining length
    num_four_min_songs = remaining_length // 4

    result = num_four_min_songs
    return result

print(solution())