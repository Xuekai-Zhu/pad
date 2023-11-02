def solution():
    
    total_time = 120 
    time_on_piano = 30
    time_writing_music = 25
    time_reading_history = 38
    time_left = total_time - time_on_piano - time_writing_music - time_reading_history
    result = time_left
    return result

print(solution())