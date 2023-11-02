def solution():
    # Define the capacity ratio of the first bowl to the second bowl
    capacity_ratio = 3/4

    # Calculate the capacity of the first bowl
    first_bowl_capacity = capacity_ratio * 600

    # Calculate the total number of marbles in both bowls
    total_marbles = first_bowl_capacity + 600
    result = total_marbles
    return result

print(solution())