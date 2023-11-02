def solution():
    middle_school_students = 50  # Given that there are 50 students in Middle School

    # Calculate the number of students in Elementary School
    elementary_school_students = 4 * middle_school_students - 3

    # Calculate the total number of students in both levels
    total_students = middle_school_students + elementary_school_students
    result = total_students
    return result

print(solution())