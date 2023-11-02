def solution():
    sandbox_length = 40
    sandbox_area = sandbox_length ** 2
    bag_coverage = 80
    bag_weight = 30

    # Calculate the total number of bags needed to fill the sandbox
    total_bags = sandbox_area / bag_coverage

    # Calculate the total weight needed to fill the sandbox
    total_weight = total_bags * bag_weight
    result = total_weight
    return result

print(solution())