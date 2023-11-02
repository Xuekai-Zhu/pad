def solution():
    internet_speed = 20  # Julia's internet speed is 20 MBps
    time = 0.5  # Half an hour is 0.5 hours
    song_size = 5  # Each song is 5 MB in size

    # Calculate the number of songs Julia can download
    # by multiplying internet speed by time and dividing by song size
    num_songs = (internet_speed * time) // song_size
    result = num_songs
    return result

print(solution())