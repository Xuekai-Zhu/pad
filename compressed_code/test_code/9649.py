def solution():
    
    
    homework_time = 30
    room_cleaning_time = homework_time / 2
    dog_walking_time = homework_time + 5
    trash_taking_time = homework_time / 6
    
    total_time_taken = homework_time + room_cleaning_time + dog_walking_time + trash_taking_time
    time_left = (2*60) - total_time_taken
    
    result = time_left
    return result

print(solution())