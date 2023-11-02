def solution():
    """With 82 students, there are 2 students for each computer. If there are 16 more students, how many computers must they have in total to continue with 2 students per computer?"""
    # Define the initial number of students and computers
    initial_students = 82
    initial_computers = initial_students // 2

    # Define the new number of students and the number of additional students
    new_students = initial_students + 16
    additional_students = new_students - initial_students

    # Calculate the new number of required computers
    new_computers = (initial_students + additional_students) // 2

    # return the result
    result = new_computers
    return result

print(solution())