def solution():
    """Jeff has 16 GB of storage on his phone. He is already using 4 GB. If a song takes up about 30MB of storage, how many songs can Jeff store on his phone? (There are 1000 MB in a GB)."""
    phone_storage = 16 * 1000  # convert GB to MB
    used_storage = 4 * 1000  # convert GB to MB
    song_size = 30  # in MB
    remaining_storage = phone_storage - used_storage
    num_songs = remaining_storage // song_size
    result = num_songs
    return result

print(solution())