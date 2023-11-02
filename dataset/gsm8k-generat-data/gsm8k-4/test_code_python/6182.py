def solution():
    """Alan counted how many chairs the office canteen has. It has 2 round tables and 2 rectangular tables. Each round table has 6 chairs, and each rectangular table has 7 chairs. How many chairs are there in all?"""
    # Define the number of chairs per round table and rectangular table
    ROUND_TABLE_CHAIRS = 6
    RECTANGULAR_TABLE_CHAIRS = 7

    # Define the number of round and rectangular tables
    num_round_tables = 2
    num_rectangular_tables = 2

    # Calculate the total number of chairs
    total_chairs = (num_round_tables * ROUND_TABLE_CHAIRS) + (num_rectangular_tables * RECTANGULAR_TABLE_CHAIRS)

    # return the result
    result = total_chairs
    return result

print(solution())