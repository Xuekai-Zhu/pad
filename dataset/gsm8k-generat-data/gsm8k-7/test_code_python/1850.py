def solution():
    bags_of_seed = 4
    coverage_per_bag = 250
    lawn_length = 22
    lawn_width = 36

    # Calculate the total area of Drew's lawn
    lawn_area = lawn_length * lawn_width

    # Calculate the total coverage provided by the bags of seed
    total_coverage = bags_of_seed * coverage_per_bag

    # Calculate the remaining square footage of lawn that can be covered by the leftover seed
    extra_coverage = total_coverage - lawn_area
    result = extra_coverage
    return result

print(solution())