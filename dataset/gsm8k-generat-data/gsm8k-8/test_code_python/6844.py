def solution():
    # Define the internet speed and time period
    internet_speed = 20  # MBps
    time_period = 0.5  # hours

    # Calculate the total data that can be downloaded in the given time period
    total_data = internet_speed * 60 * 60 * time_period  

    # Calculate the size of one song
    song_size = 5  # MB

    # Calculate the number of songs that can be downloaded in the given time period
    num_songs = total_data // song_size

    result = num_songs
    return result

print(solution())