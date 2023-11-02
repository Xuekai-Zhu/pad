def solution():
    """A party venue has 4 tables that seat 6 people each, 16 tables that seat 4 people each, and 8 round tables that seat 10 people each. What is the total capacity of all the tables at the party venue?"""
    # Define the number of seats per table
    TABLE_6_CAPACITY = 6
    TABLE_4_CAPACITY = 4
    ROUND_TABLE_CAPACITY = 10

    # Define the number of tables of each type
    num_table_6 = 4
    num_table_4 = 16
    num_round_table = 8

    # Calculate the total capacity of the tables
    total_capacity = (num_table_6 * TABLE_6_CAPACITY) + (num_table_4 * TABLE_4_CAPACITY) + (num_round_table * ROUND_TABLE_CAPACITY)

    # Display the total capacity
    result = total_capacity
    return result

print(solution())