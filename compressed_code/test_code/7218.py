def solution():
    
    total_students = 90
    cafeteria_students = (2/3) * total_students
    picnic_students = total_students - cafeteria_students
    picnic_students_moved = (1/3) * picnic_students
    cafeteria_students_moved = 3
    new_cafeteria_students = cafeteria_students + picnic_students_moved - cafeteria_students_moved
    result = new_cafeteria_students
    return result

print(solution())