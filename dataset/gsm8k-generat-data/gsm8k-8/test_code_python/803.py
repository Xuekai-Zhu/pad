def solution():
    # Calculate the number of packages needed for each theme
    vampire_packages = 11 // 5
    if 11 % 5 != 0:
        vampire_packages += 1
    pumpkin_packages = 14 // 5
    if 14 % 5 != 0:
        pumpkin_packages += 1

    # Calculate the total cost of packages and individual bags
    package_cost = (vampire_packages + pumpkin_packages) * 3
    vampire_individual_cost = (11 % 5) * 1
    pumpkin_individual_cost = (14 % 5) * 1
    individual_cost = vampire_individual_cost + pumpkin_individual_cost

    # Calculate the total cost
    total_cost = package_cost + individual_cost
    result = total_cost
    return result

print(solution())