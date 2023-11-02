def solution():
    
    total_storage = 16 * 1000 
    used_storage = 4 * 1000 
    available_storage = total_storage - used_storage
    song_size = 30
    songs = available_storage // song_size
    result = songs
    return result

print(solution())