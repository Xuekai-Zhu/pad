def solution():
    total_storage = 16 * 1000  # Jeff has 16 GB of storage, which is equal to 16,000 MB
    used_storage = 4 * 1000  # Jeff is already using 4 GB of storage, which is equal to 4,000 MB
    remaining_storage = total_storage - used_storage  # Jeff has this much storage space remaining

    # Calculate the number of songs Jeff can store on his phone
    song_size = 30  # Each song takes up about 30 MB of storage
    songs_stored = remaining_storage // song_size
    result = songs_stored
    return result

print(solution())