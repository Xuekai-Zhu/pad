def solution():
    num_vans = 6
    num_minibusses = 4
    num_students_per_van = 10
    num_students_per_minibus = 24

    # Calculate the total number of students from the vans
    total_students_from_vans = num_vans * num_students_per_van

    # Calculate the total number of students from the minibusses
    total_students_from_minibusses = num_minibusses * num_students_per_minibus

    # Calculate the total number of students on the field trip
    total_students = total_students_from_vans + total_students_from_minibusses
    result = total_students
    return result

print(solution())