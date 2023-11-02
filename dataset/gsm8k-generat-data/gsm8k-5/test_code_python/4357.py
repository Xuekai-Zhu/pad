def solution():
    num_tables = 15  # There are 15 tables in the cafeteria
    seats_per_table = 10  # Each table can seat 10 people
    empty_seats_percentage = 1/10  # 1/10 of the seats are left unseated

    # Calculate the total number of seats in the cafeteria
    total_seats = num_tables * seats_per_table

    # Calculate the number of empty seats
    empty_seats = total_seats * empty_seats_percentage

    # Calculate the number of seats taken
    seats_taken = total_seats - empty_seats
    result = seats_taken
    return result

print(solution())