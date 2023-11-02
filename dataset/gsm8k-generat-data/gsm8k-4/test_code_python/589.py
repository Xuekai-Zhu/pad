def solution():
    """A library has 7 rectangular tables and the remaining tables will be square tables. A rectangular table seats 10 pupils while a square table seats 4 pupils. How many square tables are needed so that 90 pupils can read at the same time?"""
    # Calculate the total number of seats provided by rectangular tables
    rectangular_seats = 7 * 10

    # Calculate the number of square tables needed to accommodate the remaining students
    square_tables = (90 - rectangular_seats) / 4

    # Round up to the nearest integer
    square_tables = int(math.ceil(square_tables))

    result = square_tables
    return result

print(solution())