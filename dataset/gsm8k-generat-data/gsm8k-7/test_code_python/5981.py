def solution():
    internet_speed = 2 # megabits per minute
    file_sizes = [80, 90, 70] # in megabits

    # Calculate the total size of all files in megabits
    total_size = sum(file_sizes)

    # Calculate the total download time in minutes
    total_download_time = total_size / internet_speed

    # Convert the total download time from minutes to hours
    total_download_time_hours = total_download_time / 60

    result = total_download_time_hours
    return result

print(solution())