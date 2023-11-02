def solution():
    num_columns = 4
    num_rows = 10
    num_buses = 6

    # Calculate the number of seats on one bus
    num_seats_per_bus = num_columns * num_rows

    # Calculate the total number of seats on all buses
    total_seats = num_seats_per_bus * num_buses

    # Calculate the number of students that can be accommodated on all buses
    num_students = total_seats
    result = num_students
    return result

print(solution())