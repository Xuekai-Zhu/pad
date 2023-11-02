def solution():
    initial_students = 82  # There are initially 82 students
    initial_computers = initial_students / 2  # There are initially 2 students per computer
    new_students = 16  # There are 16 more students

    # Calculate the new total number of students
    total_students = initial_students + new_students

    # Calculate the total number of computers needed
    total_computers = total_students / 2  # There will still be 2 students per computer

    result = total_computers
    return result

print(solution())