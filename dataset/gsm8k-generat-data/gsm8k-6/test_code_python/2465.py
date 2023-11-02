def solution():
    # Calculate the total number of twigs the bird needs for its nest
    total_twigs = 12 + (12 * 6)  # 12 twigs already in the circle, for each twig the bird wants to weave in 6 more to fill out the nest
    tree_twigs = total_twigs / 3  # a tree has dropped a third of the twigs the bird needs
    remaining_twigs = total_twigs - tree_twigs  # calculate the number of twigs the bird still needs to find
    result = remaining_twigs
    return result

print(solution())