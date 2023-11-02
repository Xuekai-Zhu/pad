def solution():
    file_size = 200  # Carla is downloading a 200 GB file
    download_speed = 2  # Carla can download 2 GB/minute
    download_time = (download_speed * 0.4) * file_size  # Carla can download 40% of the way through the download
    download_time += 20  # Carla has to restart the download from the beginning

    result = download_time
    return result

print(solution())