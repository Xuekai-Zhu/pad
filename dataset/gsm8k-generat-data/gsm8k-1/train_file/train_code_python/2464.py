def solution():
    """A bird is building a nest from twigs. The bird has put twelve twigs together already to make a circle. For each twig it placed into the circle, it wants to weave in six more twigs to fill out the nest. It knows a tree that has dropped a third of the twigs it needs. How many twigs will the bird still need to find to finish its nest?"""
    twigs_per_circle = 12
    extra_twigs_per_twig = 6
    total_twigs_needed = (twigs_per_circle + (twigs_per_circle * extra_twigs_per_twig))
    tree_twigs_dropped = total_twigs_needed / 3
    remaining_twigs_needed = total_twigs_needed - tree_twigs_dropped
    result = remaining_twigs_needed
    return result

print(solution())