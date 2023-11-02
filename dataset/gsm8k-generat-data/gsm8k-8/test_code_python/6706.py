def solution():
    # Calculate the total number of students and the number in Grade 6
    total_students = 100
    grade4_students = 30
    grade5_students = 35
    grade6_students = total_students - grade4_students - grade5_students
    
    result = grade6_students
    return result

print(solution())