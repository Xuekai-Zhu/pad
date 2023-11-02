def solution():
    # Calculate the number of marbles in each bag
    marbles_per_bag = 28 // 4  # // is used for integer division

    # Calculate the number of marbles left after giving away one bag
    marbles_left = (4 - 1) * marbles_per_bag

    result = marbles_left
    return result

print(solution())