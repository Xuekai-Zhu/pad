def solution():
    num_boys_grade2 = 20
    num_girls_grade2 = 11

    # Calculate the total number of students in grade 2
    total_students_grade2 = num_boys_grade2 + num_girls_grade2

    # Calculate the total number of students in grade 3
    total_students_grade3 = 2 * total_students_grade2

    # Calculate the total number of students in grades 2 and 3
    total_students = total_students_grade2 + total_students_grade3
    result = total_students
    return result

print(solution())