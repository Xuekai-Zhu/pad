def solution():
    beef = 10
    noodles_per_beef = 2
    noodles_already_have = 4
    noodles_per_package = 2

    # Calculate the total amount of noodles needed for the lasagna
    total_noodles_needed = beef * noodles_per_beef

    # Subtract the amount of noodles already have from the total
    noodles_left_to_buy = total_noodles_needed - noodles_already_have

    # Divide the remaining noodles needed by the amount in each package
    num_packages_needed = noodles_left_to_buy / noodles_per_package

    # Round up to get the actual number of packages needed
    num_packages_needed = math.ceil(num_packages_needed)
    result = num_packages_needed
    return result

print(solution())