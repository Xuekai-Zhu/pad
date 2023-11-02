def solution():
    # Calculate the initial number of students in the class
    num_tables = 6
    num_students_per_table = 3
    initial_num_students = num_tables * num_students_per_table

    # Subtract the number of students currently missing from class
    num_students_missing = 3 + 3*3 + 2*4  # 3 girls went to the bathroom, 3 times more students went to the canteen, 2 groups of 4 students each are not in class, and 9 foreign exchange students are not in class
    actual_num_students = initial_num_students - num_students_missing
    result = actual_num_students
    return result

print(solution())