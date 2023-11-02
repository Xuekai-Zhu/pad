def solution():
    num_tables_seating_6 = 4
    num_people_seating_6 = 6

    num_tables_seating_4 = 16
    num_people_seating_4 = 4

    num_round_tables_seating_10 = 8
    num_people_seating_10 = 10

    # Calculate the total seating capacity of all 6-person tables
    total_seating_capacity_6 = num_tables_seating_6 * num_people_seating_6

    # Calculate the total seating capacity of all 4-person tables
    total_seating_capacity_4 = num_tables_seating_4 * num_people_seating_4

    # Calculate the total seating capacity of all round tables
    total_seating_capacity_round = num_round_tables_seating_10 * num_people_seating_10

    # Calculate the total seating capacity of all tables
    total_seating_capacity = total_seating_capacity_6 + total_seating_capacity_4 + total_seating_capacity_round
    result = total_seating_capacity
    return result

print(solution())