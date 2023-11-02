def solution():
    """Jeff has 16 GB of storage on his phone. He is already using 4 GB. If a song takes up about 30MB of storage, how many songs can Jeff store on his phone? (There are 1000 MB in a GB)."""
    # Define the total storage and used storage in MB
    total_storage = 16 * 1000
    used_storage = 4 * 1000

    # Define the size of a song in MB
    song_size = 30

    # Calculate the available storage in MB
    available_storage = total_storage - used_storage

    # Calculate the number of songs Jeff can store
    num_songs = available_storage // song_size

    # Display the number of songs Jeff can store
    result = num_songs
    return result

print(solution())