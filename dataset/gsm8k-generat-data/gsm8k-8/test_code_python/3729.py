def solution():
    # Calculate the total time of the 3-minute songs
    time_3min_songs = 10 * 3

    # Calculate the total time of the 2-minute songs
    time_2min_songs = 15 * 2

    # Calculate the total time of the current playlist
    total_time = time_3min_songs + time_2min_songs

    # Calculate the remaining time needed in the playlist
    remaining_time = 100 - total_time
    result = remaining_time
    return result

print(solution())