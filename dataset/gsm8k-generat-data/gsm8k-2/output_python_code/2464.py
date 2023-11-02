def solution():
    """A bird is building a nest from twigs. The bird has put twelve twigs together already to make a circle. For each twig it placed into the circle, it wants to weave in six more twigs to fill out the nest. It knows a tree that has dropped a third of the twigs it needs. How many twigs will the bird still need to find to finish its nest?"""
    starting_twigs = 12
    extra_twigs_per_twigs = 6
    total_twigs_needed = starting_twigs + (starting_twigs * extra_twigs_per_twigs)
    dropped_twigs = total_twigs_needed / 3
    remaining_twigs_needed = total_twigs_needed - dropped_twigs
    twigs_to_find = remaining_twigs_needed - starting_twigs
    result = twigs_to_find
    return result

print(solution())