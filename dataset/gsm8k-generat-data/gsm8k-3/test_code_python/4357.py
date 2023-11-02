def solution():
    """There are 15 tables in the school's cafeteria. Each table can seat 10 people. Usually, only 1/10 of the seats are left unseated. How many seats are usually taken?"""
    # Define the number of tables and seats per table
    NUM_TABLES = 15
    SEATS_PER_TABLE = 10

    # Calculate the total number of seats
    total_seats = NUM_TABLES * SEATS_PER_TABLE

    # Calculate the number of seats left unseated
    unseated_seats = total_seats // 10

    # Calculate the number of seats usually taken
    taken_seats = total_seats - unseated_seats

    # Display the number of seats usually taken
    result = taken_seats
    return result

print(solution())