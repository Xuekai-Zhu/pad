def solution():
    
    num_3_min_songs = 10
    num_2_min_songs = 15
    total_time = 100
    current_playlist_time = (num_3_min_songs * 3) + (num_2_min_songs * 2)
    needed_playlist_time = total_time - current_playlist_time
    result = needed_playlist_time
    return result

print(solution())