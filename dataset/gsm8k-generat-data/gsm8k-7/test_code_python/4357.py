def solution():
    num_tables = 15
    seats_per_table = 10
    unseated_percent = 0.1

    # Calculate the total number of seats in the cafeteria
    total_seats = num_tables * seats_per_table

    # Calculate the number of seats that are usually taken
    seats_taken = total_seats - (total_seats * unseated_percent)
    result = seats_taken
    return result

print(solution())