def solution():
    """A type C school bus contains 13 rows of seats, with an aisle running down the middle of the bus, splitting each row into two sections. If the school only allowed two students to sit in each section, how many students could be seated on the bus?"""
    rows = 13
    sections_per_row = 2
    students_per_section = 2
    total_students = rows * sections_per_row * students_per_section
    result = total_students
    return result

print(solution())