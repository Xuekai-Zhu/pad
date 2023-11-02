def solution():
    
    total_students = 400
    tall_students = 90
    short_students = (2/5) * total_students
    avg_height_students = total_students - tall_students - short_students
    result = avg_height_students
    return result

print(solution())