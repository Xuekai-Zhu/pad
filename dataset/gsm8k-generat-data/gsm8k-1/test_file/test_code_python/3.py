def solution():
    """Carla is downloading a 200 GB file. Normally she can download 2 GB/minute, but 40% of the way through the download, Windows forces a restart to install updates, which takes 20 minutes. Then Carla has to restart the download from the beginning. How long does it take to download the file?"""
    file_size = 200  # in GB
    normal_speed = 2  # in GB/minute
    half_file = 0.4 * file_size  # amount downloaded before restart
    time_before_restart = half_file / normal_speed  # in minutes
    time_after_restart = file_size / normal_speed  # in minutes, starting from 0%
    time_spent = time_before_restart + 20 + time_after_restart
    result = time_spent
    return result

print(solution())