def solution():
    
    # Define the initial number of students
    initial_students = 10

    # Calculate the number of students on campus after one year
    students_after_year = initial_students * 2 ** 4

    # Calculate the number of additional students after May
    additional_students = students_after_year - initial_students

    # Display the number of additional students
    result = additional_students
    return result

print(solution())