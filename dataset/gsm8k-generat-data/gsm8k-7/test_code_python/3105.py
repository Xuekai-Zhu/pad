def solution():
    num_rows = 13
    num_sections_per_row = 2
    num_students_per_section = 2

    # Calculate the total number of sections on the bus
    total_sections = num_rows * num_sections_per_row

    # Calculate the total number of students that can be seated on the bus
    total_students = total_sections * num_students_per_section
    result = total_students
    return result

print(solution())