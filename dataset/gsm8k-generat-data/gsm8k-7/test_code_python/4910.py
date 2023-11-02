def solution():
    num_devices = 50
    cost_1 = 40
    covers_1 = 5
    cost_2 = 60
    covers_2 = 10

    # Calculate the number of packages needed for each software
    num_packages_1 = (num_devices + covers_1 - 1) // covers_1
    num_packages_2 = (num_devices + covers_2 - 1) // covers_2

    # Calculate the total cost for each software
    total_cost_1 = num_packages_1 * cost_1
    total_cost_2 = num_packages_2 * cost_2

    # Calculate the savings by choosing the $60 software package
    savings = total_cost_1 - total_cost_2
    result = savings
    return result

print(solution())