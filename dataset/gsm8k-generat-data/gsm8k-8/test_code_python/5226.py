def solution():
    # Calculate the capacity of each type of table
    table1_capacity = 6
    table2_capacity = 4
    table3_capacity = 10

    # Calculate the total capacity of each type of table
    table1_total_capacity = 4 * table1_capacity
    table2_total_capacity = 16 * table2_capacity
    table3_total_capacity = 8 * table3_capacity

    # Calculate the total capacity of all the tables
    total_capacity = table1_total_capacity + table2_total_capacity + table3_total_capacity
    result = total_capacity
    return result

print(solution())