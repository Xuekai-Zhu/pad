def solution():
    """Stan makes a playlist for the next time he goes running. He has 10 3-minute songs and 15 2-minute songs on his playlist. His entire run takes 100 minutes. If Stan wants a playlist to cover his entire run, how many more minutes of songs will he need in his playlist?"""
    total_time = 100
    song1_time = 3
    song2_time = 2
    song1_count = 10
    song2_count = 15
    playlist_time = (song1_time * song1_count) + (song2_time * song2_count)
    remaining_time = total_time - playlist_time
    result = remaining_time
    return result

print(solution())