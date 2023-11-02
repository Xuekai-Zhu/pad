def solution():
    # Calculate the number of students in the second and first schools
    num_students_second_school = 200 + 40  # the second school has 40 more students than the third school
    num_students_first_school = 2 * num_students_second_school  # the first school has twice as many students as the second school

    # Calculate the total number of students on the stage
    total_students = num_students_first_school + num_students_second_school + 200  # add up all three schools

    result = total_students
    return result

print(solution())