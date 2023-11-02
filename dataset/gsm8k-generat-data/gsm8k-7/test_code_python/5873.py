def solution():
    num_classrooms = 4
    num_boys = 56
    num_girls = 44

    # Calculate the total number of students in each classroom (assuming equal numbers of boys and girls)
    total_students = (num_boys + num_girls) / (num_classrooms * 2)
    result = total_students
    return result

print(solution())