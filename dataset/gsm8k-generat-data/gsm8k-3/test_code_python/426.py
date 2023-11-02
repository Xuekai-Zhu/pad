def solution():
    """There is three less than four times the number of students in Elementary School as there are in Middle School.  If the number of students in Middle school is 50, calculate the total number of students in both levels."""
    # Calculate the number of students in Elementary School
    elementary_students = 4 * 50 - 3

    # Calculate the total number of students
    total_students = elementary_students + 50

    # Display the total number of students
    result = total_students
    return result

print(solution())