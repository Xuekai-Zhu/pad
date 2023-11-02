def solution():
    """Julia's internet speed is 20 MBps (megabytes per second). How many songs she can download in half an hour if the size per song is 5MB?"""
    # Define the internet speed and the size of each song
    internet_speed = 20  # in MBps
    song_size = 5  # in MB

    # Calculate the total data that can be downloaded in 30 minutes
    download_amount = internet_speed * 60 * 30  # in MB

    # Calculate the number of songs that can be downloaded
    num_songs = download_amount // song_size

    # Return the result
    result = num_songs
    return result

print(solution())