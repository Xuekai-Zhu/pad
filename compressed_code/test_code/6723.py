def solution():
    
    time_pickup = 5
    time_vacuum = 20
    time_windows = 15
    time_dusting = 10
    total_cleaning_time = (time_pickup + time_vacuum + time_windows + time_dusting) * 4
    result = total_cleaning_time
    return result

print(solution())