def solution():
    """Two bowls are holding marbles, and the first bowl has a capacity equal to 3/4 the capacity of the second bowl. If the second bowl has 600 marbles, calculate the total number of marbles both bowls are holding together."""
    # Define the capacity ratio of the two bowls
    capacity_ratio = 3/4

    # Calculate the capacity of the first bowl
    second_bowl_capacity = 600
    first_bowl_capacity = capacity_ratio * second_bowl_capacity

    # Calculate the total number of marbles in both bowls
    total_marbles = first_bowl_capacity + second_bowl_capacity

    # return the result
    result = total_marbles
    return result

print(solution())