def solution():
    # Define the number of vans and minibusses
    num_vans = 6
    num_minibusses = 4

    # Calculate the number of students on the vans and minibusses
    students_on_vans = 10 * num_vans
    students_on_minibusses = 24 * num_minibusses

    # Calculate the total number of students on the field trip
    total_students = students_on_vans + students_on_minibusses
    result = total_students
    return result

print(solution())