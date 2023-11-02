def solution():
    """Julia's internet speed is 20 MBps (megabytes per second). How many songs she can download in half an hour if the size per song is 5MB?"""
    internet_speed = 20  # MBps
    time_in_seconds = 1800  # 30 minutes = 1800 seconds
    song_size = 5  # MB
    total_size = internet_speed * time_in_seconds
    songs_downloaded = total_size // song_size
    result = songs_downloaded
    return result

print(solution())