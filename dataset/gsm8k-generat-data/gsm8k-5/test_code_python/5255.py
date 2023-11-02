def solution():
    total_slices = 16 * 2  # Phoebe has two pizzas with 16 slices each
    num_friends = 3  # Phoebe is sharing the pizzas with three friends

    # Calculate the number of slices each friend eats
    friend_slices = (total_slices - 1 - 7) / (num_friends - 1)

    result = friend_slices
    return result

print(solution())