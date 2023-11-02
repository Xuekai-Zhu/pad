def solution():
    # Calculate the number of sections in one row
    sections_per_row = 2

    # Calculate the number of sections in the entire bus
    total_sections = sections_per_row * 13

    # Calculate the number of students that can sit in each section
    students_per_section = 2

    # Calculate the total number of students that can be seated
    total_students = total_sections * students_per_section
    result = total_students
    return result

print(solution())