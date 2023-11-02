def solution():
    initial_twigs = 12
    twigs_per_circle = 6
    missing_twigs_percent = 1/3

    # Calculate the total number of twigs needed for the nest
    total_twigs = initial_twigs + (initial_twigs * twigs_per_circle)

    # Calculate the number of missing twigs
    missing_twigs = int(total_twigs * missing_twigs_percent)

    # Calculate the number of twigs the bird still needs to find
    remaining_twigs = total_twigs - missing_twigs
    result = remaining_twigs
    return result

print(solution())