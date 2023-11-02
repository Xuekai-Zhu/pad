def solution():
    num_tables = 6
    students_per_table = 3
    num_girls_bathroom = 3
    num_students_canteen = num_girls_bathroom * 3
    num_new_students = 2 * 4
    num_foreign_exchange = 3 + 3 + 3

    # Calculate the total number of students currently in class
    current_students = num_tables * students_per_table - num_girls_bathroom - num_students_canteen

    # Calculate the total number of students who are not in class
    missing_students = num_new_students + num_foreign_exchange

    # Calculate the total number of students in the class
    total_students = current_students + missing_students
    result = total_students
    return result

print(solution())