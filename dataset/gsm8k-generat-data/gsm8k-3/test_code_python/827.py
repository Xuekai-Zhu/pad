def solution():
    """There are six chairs in each row in a church. If there are 20 rows of chairs in the church, and each chair holds five people, calculate the number of people who have to sit in the chairs for the church to be full."""
    # Define the number of chairs per row
    chairs_per_row = 6

    # Define the number of rows
    num_rows = 20

    # Define the number of people each chair can hold
    people_per_chair = 5

    # Calculate the total number of people the chairs can hold
    total_capacity = chairs_per_row * num_rows * people_per_chair

    # Display the total number of people the chairs can hold
    result = total_capacity
    return result

print(solution())