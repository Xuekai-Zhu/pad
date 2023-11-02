def solution():
    """Jeff has 16 GB of storage on his phone. He is already using 4 GB. If a song takes up about 30MB of storage, how many songs can Jeff store on his phone? (There are 1000 MB in a GB)."""
    # Define the total storage and the amount already used
    total_storage = 16 * 1000 # in MB
    used_storage = 4 * 1000 # in MB

    # Calculate the remaining storage
    remaining_storage = total_storage - used_storage

    # Calculate the number of songs that can be stored
    song_size = 30 # in MB
    num_songs = remaining_storage // song_size

    result = num_songs
    return result

print(solution())