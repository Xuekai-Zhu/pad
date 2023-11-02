def solution():
    
    total_students = 60
    cafeteria_students = 10
    lunch_bringers = cafeteria_students * 3
    no_lunch = total_students - cafeteria_students - lunch_bringers
    result = no_lunch
    return result

print(solution())