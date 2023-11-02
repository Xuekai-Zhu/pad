def solution():
    """With 82 students, there are 2 students for each computer. If there are 16 more students, how many computers must they have in total to continue with 2 students per computer?"""
    # Calculate the initial number of computers
    initial_computers = 82 // 2

    # Calculate the new number of students
    new_students = 82 + 16

    # Calculate the new number of computers needed
    new_computers = new_students // 2

    # Display the new number of computers needed
    result = new_computers
    return result

print(solution())