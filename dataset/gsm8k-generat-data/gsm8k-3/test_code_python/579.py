def solution():
    """Rylee is bored and decides to count the number of leaves falling off the tree in her backyard. 7 leaves fall in the first hour. For the second and third hour, the leaves fall at a rate of 4 per hour. What is the average number of leaves which fell per hour?"""
    # Define the number of leaves fallen in each hour
    hour1 = 7
    hour2 = 4
    hour3 = 4

    # Calculate the total number of leaves fallen
    total_leaves = hour1 + hour2 + hour3

    # Calculate the average number of leaves fallen per hour
    average_leaves = total_leaves / 3

    # Display the average number of leaves fallen per hour
    result = average_leaves
    return result

print(solution())