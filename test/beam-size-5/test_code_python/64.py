def solution():
    num_girls = 60
    num_boys = num_girls * 2
    num_students_per_teacher = 5

    # Calculate the total number of teachers
    total_teachers = num_girls + num_boys + num_students_per_teacher
    result = total_teachers
    return result

print(solution())