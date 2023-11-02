def solution():
    last_year_distance = 300
    current_year_distance = 4 * last_year_distance
    num_tables = 6

    # Calculate the total distance between the tables
    total_distance_between_tables = current_year_distance / (num_tables - 1)

    # Calculate the distance between table 1 and table 3
    distance_between_table_1_and_3 = 2 * total_distance_between_tables
    result = distance_between_table_1_and_3
    return result

print(solution())