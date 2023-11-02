def solution():
    # Define the number of columns and rows per bus
    columns = 4
    rows = 10

    # Calculate the total number of seats per bus
    seats_per_bus = columns * rows

    # Calculate the total number of students the buses can accommodate
    total_students = seats_per_bus * 6
    result = total_students
    return result

print(solution())