def solution():
    """Kira wants some new music on her phone. She downloads 10 songs in the morning. Later on that day, she finds 15 more songs she likes so she downloads them, and at night a friend of hers recommends 3 more songs she also downloads. Knowing that each song has a size of 5 MB, how much memory space in MB will the new songs occupy?"""
    # Define the number of songs downloaded
    songs_downloaded = 10 + 15 + 3

    # Define the size of each song in MB
    song_size = 5

    # Calculate the total memory space occupied by the new songs
    total_space = songs_downloaded * song_size

    # return the result
    result = total_space
    return result

print(solution())