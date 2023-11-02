def solution():
    
    initial_students = 10
    other_class_students = initial_students
    total_students = initial_students + other_class_students
    chaperones = 5
    teachers = 2
    total_people = total_students + chaperones + teachers
    people_left = total_people - 10 - 2
    result = people_left
    return result

print(solution())