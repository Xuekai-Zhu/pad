def solution():
    """A school bus has 4 columns and 10 rows of seats. If the school has 6 buses, how many students can the buses accommodate?"""
    # Define the number of columns and rows in each bus
    columns = 4
    rows = 10

    # Calculate the total number of seats in each bus
    total_seats = columns * rows

    # Calculate the total number of seats in all 6 buses
    total_students = total_seats * 6

    # return the result
    result = total_students
    return result

print(solution())