def solution():
    twigs_per_circle = 12  # The bird has put 12 twigs together already to make a circle
    twigs_to_add_per_circle = 6  # For each twig it placed into the circle, it wants to weave in 6 more twigs to fill out the nest
    circles_needed = 3  # The bird needs 3 circles to finish the nest
    twigs_needed = (twigs_per_circle + (twigs_to_add_per_circle * twigs_per_circle)) * circles_needed  # Total number of twigs needed
    twigs_dropped_by_tree = twigs_needed / 3  # The tree has dropped a third of the twigs the bird needs
    twigs_to_find = twigs_needed - twigs_dropped_by_tree  # Number of twigs the bird still needs to find to finish its nest
    result = twigs_to_find
    return result

print(solution())