def solution():
    # Calculate the number of songs Julia can download in half an hour
    songs_downloaded = 20 * 60 * 30 / 5  # internet speed in MBps * 60 seconds * 30 minutes / size per song in MB
    result = songs_downloaded
    return result

print(solution())