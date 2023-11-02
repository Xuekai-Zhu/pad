def solution():
    # Calculate the remaining storage that Jeff has in MB
    remaining_storage = (16 - 4) * 1000  # 1 GB is equal to 1000 MB
    
    # Calculate the number of songs that Jeff can store
    song_size = 30  # in MB
    num_songs = remaining_storage // song_size
    
    result = num_songs
    return result

print(solution())