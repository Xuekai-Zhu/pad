def solution():
    
    practice_time = 2 
    shooting_time = practice_time / 2
    other_time = practice_time - shooting_time
    running_time = other_time * 2 / 3
    weightlifting_time = other_time / 3
    weightlifting_time_minutes = weightlifting_time * 60
    result = weightlifting_time_minutes
    return result

print(solution())