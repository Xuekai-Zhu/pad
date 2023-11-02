def solution():
    total_people = 45 + 123  # Total number of people at the reunion
    num_tables = 14  # Number of tables available

    # Calculate the number of people at each table
    people_per_table = total_people / num_tables
    result = people_per_table
    return result

print(solution())