def solution():
    
    total_questions = 80
    remaining_questions = total_questions - 16
    remaining_time = (remaining_questions / 64) * 48
    total_time = 60
    time_left = total_time - remaining_time - 12
    result = time_left
    return result

print(solution())