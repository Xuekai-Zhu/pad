def solution():
    # Calculate the total size of the files Cortney is downloading
    total_size = 80 + 90 + 70  # in megabits

    # Calculate the time it will take to download all the files
    time_in_minutes = total_size / 2  # her internet speed is 2 megabits per minute
    time_in_hours = time_in_minutes / 60
    
    result = time_in_hours
    return result

print(solution())