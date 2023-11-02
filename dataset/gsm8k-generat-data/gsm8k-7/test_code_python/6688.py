def solution():
    num_students = 82
    students_per_computer = 2
    new_num_students = num_students + 16

    # Calculate the number of computers needed for the original number of students
    num_computers = num_students / students_per_computer

    # Calculate the number of computers needed for the new number of students
    new_num_computers = new_num_students / students_per_computer

    # Calculate the total number of computers needed
    total_num_computers = new_num_computers

    result = total_num_computers
    return result

print(solution())