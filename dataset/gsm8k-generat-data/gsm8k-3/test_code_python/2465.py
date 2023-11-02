def solution():
    """A bird is building a nest from twigs. The bird has put twelve twigs together already to make a circle. For each twig it placed into the circle, it wants to weave in six more twigs to fill out the nest. It knows a tree that has dropped a third of the twigs it needs. How many twigs will the bird still need to find to finish its nest?"""
    # Define the initial number of twigs in the nest
    initial_twigs = 12

    # Define the number of twigs needed for each additional weave
    additional_twigs = 6

    # Define the total number of twigs needed for the nest
    total_twigs = initial_twigs + (initial_twigs * additional_twigs)

    # Calculate the number of twigs the tree has dropped
    dropped_twigs = total_twigs / 3

    # Calculate the number of twigs the bird still needs to find
    remaining_twigs = total_twigs - dropped_twigs

    # Display the number of twigs the bird still needs to find
    result = remaining_twigs
    return result

print(solution())