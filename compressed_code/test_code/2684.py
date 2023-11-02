def solution():
    
    total_students = 24
    first_group = 5
    second_group = 8
    third_group = 7
    fourth_group = total_students - first_group - second_group - third_group
    result = fourth_group
    return result

print(solution())