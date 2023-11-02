def solution():
    
    current_num_students = 960
    percent_increase = 20
    
    original_num_students = current_num_students / (1 + percent_increase/100)
    
    original_num_students = round(original_num_students)
    result = original_num_students
    return result

print(solution())