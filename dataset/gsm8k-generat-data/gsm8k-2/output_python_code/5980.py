def solution():
    """Cortney is downloading some files to her computer. Her internet speed is 2 megabits per minute. If she can download the files one at a time and the files she is downloading have the size of 80 megabits, 90 megabits, and 70 megabits. How many hours will it take for her to download all of it?"""
    file_sizes = [80, 90, 70]
    download_speed = 2
    total_download_time = sum(file_sizes) / download_speed
    total_hours = total_download_time / 60
    result = total_hours
    return result

print(solution())