def solution():
    # Calculate the amount of noodles needed
    noodles_needed = 2 * 10

    # Calculate the amount of additional noodles needed
    additional_noodles_needed = noodles_needed - 4

    # Calculate the number of packages needed
    packages_needed = additional_noodles_needed / 2

    result = packages_needed
    return result

print(solution())