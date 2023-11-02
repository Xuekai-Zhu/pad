def solution():
    """For a wedding, chairs were arranged in 7 rows with 12 chairs in each row. Some people arrived late and grabbed 11 extra chairs, placing them at the back. How many chairs were there altogether?"""
    # Define the number of rows and chairs in each row
    rows = 7
    chairs_per_row = 12

    # Calculate the initial number of chairs
    initial_chairs = rows * chairs_per_row

    # Add the extra chairs that were grabbed
    total_chairs = initial_chairs + 11

    result = total_chairs
    return result

print(solution())