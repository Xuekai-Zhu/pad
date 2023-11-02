def solution():
    devices_needed = 50
    package_1_cost = 40
    package_1_coverage = 5
    package_2_cost = 60
    package_2_coverage = 10
    packages_needed_1 = devices_needed / package_1_coverage
    packages_needed_2 = devices_needed / package_2_coverage
    total_cost_1 = packages_needed_1 * package_1_cost
    total_cost_2 = packages_needed_2 * package_2_cost
    savings = total_cost_1 - total_cost_2
    result = savings
    return result

print(solution())