def solution():
    total_students = 92
    bus_riders = 20
    remaining_students = total_students - bus_riders
    bike_riders = (5/8) * remaining_students
    walking_students = remaining_students - bike_riders

    result = walking_students
    return result

print(solution())