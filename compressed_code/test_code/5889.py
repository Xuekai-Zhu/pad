def solution():
    
    total_students = 40
    absent_percent = 1/10
    present_students = total_students - (total_students * absent_percent)
    classroom_percent = 3/4
    classroom_students = present_students * classroom_percent
    canteen_students = present_students - classroom_students
    result = canteen_students
    return result

print(solution())