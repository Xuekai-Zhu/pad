def solution():
    """A school bus has 4 columns and 10 rows of seats. If the school has 6 buses, how many students can the buses accommodate?"""
    # Define the number of columns and rows in each bus
    COLUMNS = 4
    ROWS = 10

    # Define the number of buses
    buses = 6

    # Calculate the total number of seats across all buses
    total_seats = COLUMNS * ROWS * buses

    # Display the total number of seats
    result = total_seats
    return result

print(solution())