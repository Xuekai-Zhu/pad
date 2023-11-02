def solution():
    """A bird is building a nest from twigs. The bird has put twelve twigs together already to make a circle. For each twig it placed into the circle, it wants to weave in six more twigs to fill out the nest. It knows a tree that has dropped a third of the twigs it needs. How many twigs will the bird still need to find to finish its nest?"""
    # Define the number of twigs in the completed nest
    completed_nest = 12 + 12*6

    # Define the number of twigs dropped by the tree
    dropped_twigs = completed_nest / 3

    # Calculate the number of twigs the bird still needs to find
    remaining_twigs = completed_nest - dropped_twigs

    # Return the result
    result = remaining_twigs
    return result

print(solution())