def solution():
    """Cortney is downloading some files to her computer. Her internet speed is 2 megabits per minute. If she can download the files one at a time and the files she is downloading have the size of 80 megabits, 90 megabits, and 70 megabits. How many hours will it take for her to download all of it?"""
    internet_speed = 2  # megabits per minute
    file_sizes = [80, 90, 70]  # in megabits
    total_size = sum(file_sizes)
    total_time_minutes = total_size / internet_speed
    total_time_hours = total_time_minutes / 60
    result = total_time_hours
    return result

print(solution())