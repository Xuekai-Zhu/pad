def solution():
    internet_speed = 2  # megabits per minute
    file_sizes = [80, 90, 70]  # megabits
    total_file_size = sum(file_sizes)  # megabits

    # Calculate the total download time in minutes
    total_download_time = total_file_size / internet_speed

    # Convert the total download time to hours
    hours = total_download_time / 60
    result = hours
    return result

print(solution())