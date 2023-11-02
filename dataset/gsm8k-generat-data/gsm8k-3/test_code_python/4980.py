def solution():
    """Two bowls are holding marbles, and the first bowl has a capacity equal to 3/4 the capacity of the second bowl. If the second bowl has 600 marbles, calculate the total number of marbles both bowls are holding together."""
    # Define the capacity ratio of the two bowls
    CAPACITY_RATIO = 3/4

    # Define the capacity and number of marbles in the second bowl
    second_bowl_capacity = 600
    second_bowl_marbles = 600

    # Calculate the capacity and number of marbles in the first bowl
    first_bowl_capacity = second_bowl_capacity / CAPACITY_RATIO
    first_bowl_marbles = first_bowl_capacity - second_bowl_marbles

    # Calculate the total number of marbles
    total_marbles = first_bowl_marbles + second_bowl_marbles

    # Display the total number of marbles
    result = total_marbles
    return result

print(solution())