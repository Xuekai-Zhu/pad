def solution():
    
    total_time = 100
    song1_time = 3
    song2_time = 2
    song1_count = 10
    song2_count = 15
    playlist_time = (song1_time * song1_count) + (song2_time * song2_count)
    remaining_time = total_time - playlist_time
    result = remaining_time
    return result

print(solution())