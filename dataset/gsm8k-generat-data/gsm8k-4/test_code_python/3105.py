def solution():
    """A type C school bus contains 13 rows of seats, with an aisle running down the middle of the bus, splitting each row into two sections.  If the school only allowed two students to sit in each section, how many students could be seated on the bus?"""
    # Define the number of rows and sections per row
    rows = 13
    sections_per_row = 2

    # Calculate the number of sections on the bus
    total_sections = rows * sections_per_row

    # Calculate the number of students that can be seated on the bus
    students = total_sections * 2

    result = students
    return result

print(solution())