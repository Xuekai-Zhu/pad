def solution():
    
    file_sizes = [80, 90, 70]
    download_speed = 2
    total_download_time = sum(file_sizes) / download_speed
    total_hours = total_download_time / 60
    result = total_hours
    return result

print(solution())