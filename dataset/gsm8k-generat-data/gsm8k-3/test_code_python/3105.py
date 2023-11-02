def solution():
    """A type C school bus contains 13 rows of seats, with an aisle running down the middle of the bus, splitting each row into two sections.  If the school only allowed two students to sit in each section, how many students could be seated on the bus?"""
    # Define the number of rows and sections in the bus
    rows = 13
    sections_per_row = 2

    # Calculate the number of sections on the bus
    total_sections = rows * sections_per_row

    # Calculate the number of students that can sit on the bus
    students_per_section = 2
    total_students = total_sections * students_per_section

    # Display the total number of students that can sit on the bus
    result = total_students
    return result

print(solution())