def solution():
    """There is three less than four times the number of students in Elementary School as there are in Middle School. If the number of students in Middle school is 50, calculate the total number of students in both levels."""
    middle_school_students = 50
    elementary_school_students = 4 * middle_school_students - 3
    total_students = middle_school_students + elementary_school_students
    result = total_students
    return result

print(solution())