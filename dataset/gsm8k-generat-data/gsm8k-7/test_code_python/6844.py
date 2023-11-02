def solution():
    internet_speed = 20 # MBps
    song_size = 5 # MB
    time_in_sec = 30 * 60 # 30 minutes in seconds

    # Calculate the total amount of data Julia can download in half an hour
    total_data = internet_speed * time_in_sec

    # Calculate the number of songs Julia can download
    num_songs = total_data / song_size
    result = num_songs
    return result

print(solution())