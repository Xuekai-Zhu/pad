def solution():
    # Calculate the total number of songs and the total memory space they occupy
    num_songs = 10 + 15 + 3  # Kira downloaded 10 songs in the morning, 15 more songs later in the day, and 3 more at night
    memory_space = num_songs * 5  # Each song has a size of 5 MB
    
    result = memory_space
    return result

print(solution())