def solution():
    # Calculate the total number of twigs needed to fill out the nest
    total_twigs_needed = (12 + 6 * 12)

    # Calculate the number of twigs dropped by the tree
    twigs_dropped = total_twigs_needed / 3

    # Calculate the number of twigs the bird still needs to find
    twigs_needed = total_twigs_needed - twigs_dropped
    result = twigs_needed
    return result

print(solution())