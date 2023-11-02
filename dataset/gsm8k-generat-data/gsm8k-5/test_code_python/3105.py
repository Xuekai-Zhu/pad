def solution():
    rows = 13  # The bus contains 13 rows of seats
    seats_per_row = 2  # Each row is split into two sections, with 2 seats in each section
    seats_per_section = seats_per_row * 2  # Each row contains 4 seats total
    total_seats = rows * seats_per_section  # The bus has this many total seats

    # Calculate the number of students that can be seated on the bus
    students_seated = total_seats // 2  # Only 2 students are allowed in each section

    result = students_seated
    return result

print(solution())