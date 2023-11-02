def solution():
    
    phone_storage = 16 * 1000  
    used_storage = 4 * 1000  
    song_size = 30  
    remaining_storage = phone_storage - used_storage
    num_songs = remaining_storage // song_size
    result = num_songs
    return result

print(solution())