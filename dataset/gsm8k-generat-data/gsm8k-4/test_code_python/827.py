def solution():
    """There are six chairs in each row in a church. If there are 20 rows of chairs in the church, and each chair holds five people, calculate the number of people who have to sit in the chairs for the church to be full."""
    # Define the number of chairs in each row and the number of rows
    chairs_per_row = 6
    num_rows = 20

    # Calculate the total number of chairs in the church
    total_chairs = chairs_per_row * num_rows

    # Calculate the total number of people who can sit in the chairs
    total_people = total_chairs * 5

    # Return the result
    result = total_people
    return result

print(solution())