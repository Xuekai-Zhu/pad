def solution():
    """Stan makes a playlist for the next time he goes running. He has 10 3-minute songs and 15 2-minute songs on his playlist. His entire run takes 100 minutes. If Stan wants a playlist to cover his entire run, how many more minutes of songs will he need in his playlist?"""
    num_3_min_songs = 10
    num_2_min_songs = 15
    total_time = 100
    current_playlist_time = (num_3_min_songs * 3) + (num_2_min_songs * 2)
    needed_playlist_time = total_time - current_playlist_time
    result = needed_playlist_time
    return result

print(solution())