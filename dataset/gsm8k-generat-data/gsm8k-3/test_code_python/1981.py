def solution():
    """Kira wants some new music on her phone. She downloads 10 songs in the morning. Later on that day, she finds 15 more songs she likes so she downloads them, and at night a friend of hers recommends 3 more songs she also downloads. Knowing that each song has a size of 5 MB, how much memory space in MB will the new songs occupy?"""
    # Define the size of each song in MB
    SONG_SIZE = 5

    # Define the number of songs downloaded in the morning, afternoon, and evening
    morning_songs = 10
    afternoon_songs = 15
    evening_songs = 3

    # Calculate the total number of songs downloaded
    total_songs = morning_songs + afternoon_songs + evening_songs

    # Calculate the total memory space required for the new songs
    total_space = total_songs * SONG_SIZE

    # Display the total memory space required
    result = total_space
    return result

print(solution())