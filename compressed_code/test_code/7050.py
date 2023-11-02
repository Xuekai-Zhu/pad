def solution():
    
    total_students = 92
    bus_students = 20
    remaining_students = total_students - bus_students
    bike_students = (5/8) * remaining_students
    walking_students = remaining_students - bike_students
    result = walking_students
    
    return result

print(solution())