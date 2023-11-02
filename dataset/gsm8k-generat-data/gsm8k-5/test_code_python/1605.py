def solution():
    total_students = 92  # There are 92 students altogether
    bus_students = 20  # Twenty students ride the bus home together
    remaining_students = total_students - bus_students  # Calculate the number of remaining students
    bike_students = int(5/8 * remaining_students)  # Calculate the number of students who ride their own bike home
    walking_students = remaining_students - bike_students  # Calculate the number of students walking home
    result = walking_students
    return result

print(solution())