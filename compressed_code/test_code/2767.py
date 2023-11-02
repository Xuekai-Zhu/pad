def solution():
    
    total_students = 60
    cafeteria_students = 10
    lunch_bringers = 3 * cafeteria_students
    no_lunch_students = total_students - cafeteria_students - lunch_bringers
    result = no_lunch_students
    return result

print(solution())