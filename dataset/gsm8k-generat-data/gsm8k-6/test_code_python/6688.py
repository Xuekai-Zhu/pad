def solution():
    # Calculate the initial number of computers needed for 82 students with 2 students per computer
    initial_computers = 82/2

    # Calculate the new number of students and the number of computers needed to accommodate them with 2 students per computer
    new_students = 82 + 16
    new_computers = new_students/2

    result = new_computers
    return result

print(solution())