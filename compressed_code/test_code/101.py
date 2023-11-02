def solution():
    
    total_students = 40
    absent_students = total_students / 10
    present_students = total_students - absent_students
    classroom_students = present_students * (3 / 4)
    canteen_students = present_students - classroom_students
    result = canteen_students
    return result

print(solution())