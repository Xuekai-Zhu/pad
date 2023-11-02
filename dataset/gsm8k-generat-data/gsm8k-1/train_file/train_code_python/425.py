def solution():
    """There is three less than four times the number of students in Elementary School as there are in Middle School. If the number of students in Middle school is 50, calculate the total number of students in both levels."""
    middle_school = 50
    elementary_school = 4 * middle_school - 3
    total_students = middle_school + elementary_school
    result = total_students
    return result

print(solution())