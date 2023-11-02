def solution():
    num_vans = 5
    students_per_van = 28
    boys = 60

    # Calculate the total number of students
    total_students = num_vans * students_per_van

    # Calculate the number of girls
    girls = total_students - boys

    result = girls
    return result

print(solution())