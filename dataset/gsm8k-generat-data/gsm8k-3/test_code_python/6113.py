def solution():
    """Jackson is buying chairs for his restaurant. He has 6 tables with 4 seats and 12 tables with 6 seats. How many chairs total does Jackson need to buy?"""
    # Define the number of tables and seats per table
    TABLES_4_SEATS = 6
    TABLES_6_SEATS = 12
    SEATS_PER_TABLE_4 = 4
    SEATS_PER_TABLE_6 = 6

    # Calculate the total number of chairs needed
    total_chairs = TABLES_4_SEATS * SEATS_PER_TABLE_4 + TABLES_6_SEATS * SEATS_PER_TABLE_6

    # Display the total number of chairs needed
    result = total_chairs
    return result

print(solution())