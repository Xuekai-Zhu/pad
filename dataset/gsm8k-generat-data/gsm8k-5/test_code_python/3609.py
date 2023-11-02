def solution():
    seats_per_bus = 4 * 10  # Each bus has 4 columns and 10 rows of seats
    num_buses = 6  # There are 6 buses in total

    # Calculate the total number of students the buses can accommodate
    total_students = seats_per_bus * num_buses
    result = total_students
    return result

print(solution())