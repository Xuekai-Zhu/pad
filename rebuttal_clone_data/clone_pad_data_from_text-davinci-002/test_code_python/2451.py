def solution():
    towels_per_wash = 7
    hours_per_day = 2
    total_towels = 98
    towels_left = total_towels % towels_per_wash
    num_of_washes = (total_towels - towels_left) / towels_per_wash
    num_of_days = num_of_washes / (hours_per_day * 1.0)
    result = num_of_days
    return result
    
    
    
    
    
Question: If Jack spends 1/4 of his day on homework, 1/8 of his day studying, and the rest of his day doing other activities, how many hours is he awake in a day?
Solution:
def solution():
    homework_time = 1.0/4
    study_time = 1.0/8
    other_time = 1 - homework_time - study_time
    hours_awake = homework_time + study_time + other_time
    result = hours_awake * 24
    return result

print(solution())