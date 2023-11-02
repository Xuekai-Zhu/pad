def solution():
    total_classrooms = 15
    classrooms_with_30_desks = total_classrooms / 3
    classrooms_with_25_desks = total_classrooms - classrooms_with_30_desks
    desks_in_30_classrooms = 30 * classrooms_with_30_desks
    desks_in_25_classrooms = 25 * classrooms_with_25_desks
    total_desks = desks_in_30_classrooms + desks_in_25_classrooms
    result = total_desks
    return result

print(solution())