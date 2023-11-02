def solution():
    total_students = 92
    bus_students = 20
    bike_students = (total_students - bus_students) * 5/8
    walk_students = total_students - bus_students - bike_students
    result = walk_students
    return result

print(solution())