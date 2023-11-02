def solution():
    # Calculate the distance of this year's relay run
    this_year_distance = 300 * 4

    # Calculate the total number of tables (including the finish line)
    total_tables = 6

    # Calculate the distance between each table
    distance_between_tables = this_year_distance / (total_tables - 1)

    # Calculate the distance between table 1 and table 3
    distance_between_1_and_3 = 2 * distance_between_tables

    result = distance_between_1_and_3
    return result

print(solution())