def solution():
    num_3rd_grade = 19  # Number of students in 3rd grade
    num_4th_grade = 2 * num_3rd_grade  # Number of students in 4th grade is twice the number in 3rd grade
    num_2nd_grade = 10 + 19  # Total number of students in 2nd grade is the sum of boys and girls

    # Calculate the total number of students
    total_students = num_3rd_grade + num_4th_grade + num_2nd_grade
    result = total_students
    return result

print(solution())