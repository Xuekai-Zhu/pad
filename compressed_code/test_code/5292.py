def solution():
    
    internet_speed = 20 
    song_size = 5 
    download_time = 30 * 60 
    total_size = internet_speed * download_time
    num_songs = total_size // song_size
    result = num_songs
    return result

print(solution())