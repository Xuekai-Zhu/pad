def solution():
    """A library has 7 rectangular tables and the remaining tables will be square tables. A rectangular table seats 10 pupils while a square table seats 4 pupils. How many square tables are needed so that 90 pupils can read at the same time?"""
    # Define the number of rectangular tables and the number of pupils they can seat
    RECTANGULAR_TABLES = 7
    RECTANGULAR_CAPACITY = 10

    # Define the number of pupils and the required capacity
    pupils = 90
    required_capacity = pupils - RECTANGULAR_TABLES * RECTANGULAR_CAPACITY

    # Calculate the number of square tables needed
    square_tables = required_capacity // 4 + (required_capacity % 4 > 0)

    # Display the number of square tables needed
    result = square_tables
    return result

print(solution())