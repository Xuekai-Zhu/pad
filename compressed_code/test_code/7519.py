def solution():
    
    num_students = 10
    avg_age_9_students = 8
    sum_age_9_students = avg_age_9_students * (num_students - 1)
    total_age = sum_age_9_students + 28
    new_avg_age = total_age / num_students
    increase_in_avg = new_avg_age - avg_age_9_students
    result = increase_in_avg
    return result

print(solution())