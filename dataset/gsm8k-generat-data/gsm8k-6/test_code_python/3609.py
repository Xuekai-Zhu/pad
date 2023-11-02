def solution():
    # Calculate the total number of seats in one bus
    seats_per_bus = 4 * 10  # 4 columns and 10 rows of seats

    # Calculate the total number of students that can be accommodated by 6 buses
    total_students = seats_per_bus * 6

    result = total_students
    return result

print(solution())