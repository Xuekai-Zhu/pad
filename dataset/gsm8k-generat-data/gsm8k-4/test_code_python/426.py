def solution():
    """There are three less than four times the number of students in Elementary School as there are in Middle School. If the number of students in Middle school is 50, calculate the total number of students in both levels."""
    # Define the number of students in middle school
    middle_school_students = 50

    # Calculate the number of students in elementary school
    elementary_school_students = 4 * middle_school_students - 3

    # Calculate the total number of students
    total_students = middle_school_students + elementary_school_students

    # Return the result
    result = total_students
    return result

print(solution())