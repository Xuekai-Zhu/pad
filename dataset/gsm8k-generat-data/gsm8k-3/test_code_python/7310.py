def solution():
    """For a wedding, chairs were arranged in 7 rows with 12 chairs in each row. Some people arrived late and grabbed 11 extra chairs, placing them at the back. How many chairs were there altogether?"""
    # Define the number of rows and chairs per row
    rows = 7
    chairs_per_row = 12

    # Calculate the total number of chairs before the late arrivals
    total_chairs = rows * chairs_per_row

    # Calculate the total number of chairs after the late arrivals
    total_chairs += 11

    # Display the total number of chairs
    result = total_chairs
    return result

print(solution())