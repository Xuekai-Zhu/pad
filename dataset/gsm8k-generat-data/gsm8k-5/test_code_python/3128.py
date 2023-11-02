def solution():
    # Calculate the total number of students on the vans
    students_per_van = 10
    total_students_on_vans = students_per_van * 6

    # Calculate the total number of students on the minibusses
    students_per_minibus = 24
    total_students_on_minibusses = students_per_minibus * 4

    # Calculate the total number of students on the field trip
    total_students = total_students_on_vans + total_students_on_minibusses
    result = total_students
    return result

print(solution())