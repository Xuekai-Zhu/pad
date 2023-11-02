def solution():
    # Define the starting number of students and the changes over each year
    start_num_students = 150
    num_students_year2 = start_num_students + 30
    num_students_year3 = num_students_year2 - 15

    # Calculate the final number of students
    final_num_students = num_students_year3
    result = final_num_students
    return result

print(solution())