def solution():
    """There are 15 tables in the school's cafeteria. Each table can seat 10 people. Usually, only 1/10 of the seats are left unseated. How many seats are usually taken?"""
    total_seats = 15 * 10
    unseated_seats = total_seats / 10
    seated_seats = total_seats - unseated_seats
    result = seated_seats
    return result

print(solution())