def solution():
    num_marbles = 28
    num_bags = 4

    # Calculate the number of marbles in each bag
    marbles_per_bag = num_marbles / num_bags

    # Calculate the number of marbles remaining after giving away one bag
    remaining_marbles = num_marbles - marbles_per_bag

    result = remaining_marbles
    return result

print(solution())