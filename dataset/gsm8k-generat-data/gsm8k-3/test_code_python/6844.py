def solution():
    """Julia's internet speed is 20 MBps (megabytes per second). How many songs she can download in half an hour if the size per song is 5MB?"""
    # Convert the internet speed to megabytes per minute
    speed = 20 * 60
    # Calculate the number of songs that can be downloaded in half an hour
    songs_downloaded = (speed * 30) // 5
    result = songs_downloaded
    return result

print(solution())