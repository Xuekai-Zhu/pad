def solution():
    num_3_minute_songs = 10
    num_2_minute_songs = 15
    total_run_time = 100

    # Calculate the total time of 3-minute songs
    total_3_minute_time = num_3_minute_songs * 3

    # Calculate the total time of 2-minute songs
    total_2_minute_time = num_2_minute_songs * 2

    # Calculate the total time of all songs on the playlist
    total_playlist_time = total_3_minute_time + total_2_minute_time

    # Calculate the remaining time needed in the playlist
    remaining_time = total_run_time - total_playlist_time
    result = remaining_time
    return result

print(solution())