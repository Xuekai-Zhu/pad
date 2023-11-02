def solution():
    # Calculate how many packages of each type are needed to cover 50 devices
    num_packages_40 = (50 // 5) + (1 if 50 % 5 != 0 else 0) # Round up to the nearest package
    num_packages_60 = (50 // 10) + (1 if 50 % 10 != 0 else 0) # Round up to the nearest package

    # Calculate the cost of each package
    cost_40 = num_packages_40 * 40
    cost_60 = num_packages_60 * 60

    # Calculate the amount saved by buying the $60 package instead of the $40 package
    savings = cost_40 - cost_60
    result = savings
    return result

print(solution())