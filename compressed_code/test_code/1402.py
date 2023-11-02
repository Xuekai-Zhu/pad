def solution():
    
    total_students = 90
    cafeteria_students = (2/3) * total_students 
    outside_students = total_students - cafeteria_students
    outside_to_cafeteria = (1/3) * outside_students
    cafeteria_to_outside = 3
    total_cafeteria = cafeteria_students + outside_to_cafeteria - cafeteria_to_outside
    result = total_cafeteria
    return result

print(solution())