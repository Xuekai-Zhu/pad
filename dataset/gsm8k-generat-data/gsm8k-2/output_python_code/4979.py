def solution():
    """Two bowls are holding marbles, and the first bowl has a capacity equal to 3/4 the capacity of the second bowl. If the second bowl has 600 marbles, calculate the total number of marbles both bowls are holding together."""
    second_bowl_capacity = 600
    first_bowl_capacity = 3/4 * second_bowl_capacity
    total_capacity = first_bowl_capacity + second_bowl_capacity
    total_marbles = total_capacity
    result = total_marbles
    return result

print(solution())