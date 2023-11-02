def solution():
    total_students = 92
    bus_students = 20
    remaining_students = total_students - bus_students

    # Calculate the number of students riding their own bike home
    bike_students = remaining_students * (5/8)

    # Calculate the number of students walking home
    walk_students = remaining_students - bike_students
    result = walk_students
    return result

print(solution())