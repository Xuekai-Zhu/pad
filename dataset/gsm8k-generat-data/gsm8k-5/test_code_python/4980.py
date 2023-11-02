def solution():
    second_bowl_capacity = 600  # Second bowl has 600 marbles
    first_bowl_capacity = 3/4 * second_bowl_capacity  # First bowl has 3/4 the capacity of the second bowl

    # Calculate the total number of marbles in both bowls
    total_marbles = first_bowl_capacity + second_bowl_capacity
    result = total_marbles
    return result

print(solution())