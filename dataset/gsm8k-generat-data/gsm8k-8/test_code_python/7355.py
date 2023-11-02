def solution():
    # Calculate the total time of the 16 three-minute songs
    total_time = 16 * 3

    # Calculate the remaining time needed for the playlist to be an hour long
    remaining_time = 60 - total_time

    # Determine how many four-minute songs can fit into the remaining time
    num_four_min_songs = remaining_time // 4

    result = num_four_min_songs
    return result

print(solution())