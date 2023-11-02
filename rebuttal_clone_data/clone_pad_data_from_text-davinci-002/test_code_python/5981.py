def solution():
    internet_speed = 2
    file_size1 = 80
    file_size2 = 90
    file_size3 = 70
    total_file_size = file_size1 + file_size2 + file_size3
    time_in_minutes = total_file_size / internet_speed
    time_in_hours = time_in_minutes / 60
    result = time_in_hours
    return result

print(solution())