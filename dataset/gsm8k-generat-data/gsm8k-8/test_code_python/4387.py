def solution():
    total_storage = 16 * 1000 # convert GB to MB
    used_storage = 4 * 1000 # convert GB to MB
    song_storage = 30 # in MB

    remaining_storage = total_storage - used_storage
    num_songs = remaining_storage // song_storage

    result = num_songs
    return result

print(solution())