def solution():
    """Jackson is buying chairs for his restaurant. He has 6 tables with 4 seats and 12 tables with 6 seats. How many chairs total does Jackson need to buy?"""
    # Define the number of tables and seats per table
    tables_4seats = 6
    tables_6seats = 12
    seats_4 = 4
    seats_6 = 6

    # Calculate the total number of chairs needed
    chairs_4 = tables_4seats * seats_4
    chairs_6 = tables_6seats * seats_6
    total_chairs = chairs_4 + chairs_6

    # return the result
    result = total_chairs
    return result

print(solution())