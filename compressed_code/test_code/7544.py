def solution():
    
    total_time = 150
    math_time = total_time * 0.3
    science_time = total_time * 0.4
    other_subjects_time = total_time - math_time - science_time
    result = other_subjects_time
    return result

print(solution())