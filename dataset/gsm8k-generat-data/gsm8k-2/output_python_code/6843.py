def solution():
    """Julia's internet speed is 20 MBps (megabytes per second). How many songs she can download in half an hour if the size per song is 5MB?"""
    internet_speed = 20 # in MBps
    song_size = 5 # in MB
    download_time = 30 * 60 # in seconds
    total_size = internet_speed * download_time
    num_songs = total_size // song_size
    result = num_songs
    return result

print(solution())