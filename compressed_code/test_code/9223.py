def solution():
    
    num_tables = 15
    seats_per_table = 10
    unseated_percent = 1/10
    seated_percent = 1 - unseated_percent
    total_seats = num_tables * seats_per_table
    taken_seats = total_seats * seated_percent
    result = taken_seats
    return result

print(solution())