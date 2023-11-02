def solution():
    
    total_classrooms = 15
    one_third = total_classrooms / 3
    thirty_desks = one_third
    twenty_five_desks = total_classrooms - thirty_desks
    total_desks = (thirty_desks * 30) + (twenty_five_desks * 25)
    total_students = total_desks
    result = total_students
    return result

print(solution())