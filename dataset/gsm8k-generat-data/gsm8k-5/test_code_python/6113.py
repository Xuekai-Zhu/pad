def solution():
    seats_per_table1 = 4  # Each of the 6 tables has 4 seats
    seats_per_table2 = 6  # Each of the 12 tables has 6 seats

    # Calculate the total number of seats needed
    total_seats_needed = (seats_per_table1 * 6) + (seats_per_table2 * 12)

    result = total_seats_needed
    return result

print(solution())