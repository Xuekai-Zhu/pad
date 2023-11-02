def solution():
    sick_students = 22
    
    # Find the total number of students in Zack's classroom (half of the total between Tina and Maura's classrooms)
    zacks_students = sick_students * 2
    
    # Find the total number of students in Tina and Maura's classrooms (since they have the same number of students)
    tina_maura_students = zacks_students * 2
    
    # Find the total number of students in all three classrooms
    total_students = tina_maura_students + zacks_students
    
    result = total_students
    return result

print(solution())