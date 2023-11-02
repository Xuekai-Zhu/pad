def solution():
    # Calculate the area of Drew's lawn
    lawn_area = 22 * 36
    # Calculate the total area covered by the four bags of seed
    total_seed_area = 4 * 250
    # Calculate the area of the lawn that will not be covered by the seed
    uncovered_area = lawn_area - total_seed_area

    result = uncovered_area
    return result

print(solution())