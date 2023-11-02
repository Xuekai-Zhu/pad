def solution():
    """There are 15 tables in the school's cafeteria. Each table can seat 10 people. Usually, only 1/10 of the seats are left unseated. How many seats are usually taken?"""
    num_tables = 15
    seats_per_table = 10
    unseated_percent = 1/10
    seated_percent = 1 - unseated_percent
    total_seats = num_tables * seats_per_table
    taken_seats = total_seats * seated_percent
    result = taken_seats
    return result

print(solution())