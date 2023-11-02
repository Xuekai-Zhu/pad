def solution():
    
    percent_below_b = 40
    total_students = 60
    students_above_b = total_students - (total_students * (percent_below_b / 100))
    result = students_above_b
    
    return result

print(solution())