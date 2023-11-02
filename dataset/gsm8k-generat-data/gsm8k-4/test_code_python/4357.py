def solution():
    """There are 15 tables in the school's cafeteria. Each table can seat 10 people. Usually, only 1/10 of the seats are left unseated. How many seats are usually taken?"""
    # Define the number of tables and the seating capacity of each table
    num_tables = 15
    table_capacity = 10

    # Calculate the total number of seats
    total_seats = num_tables * table_capacity

    # Calculate the number of seats left unseated
    unseated_seats = total_seats * (1/10)

    # Calculate the number of seats usually taken
    taken_seats = total_seats - unseated_seats

    result = taken_seats
    return result

print(solution())