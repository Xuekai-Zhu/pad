def solution():
    sandwiches_per_person = 2  # Margaret wants each person on the committee to have 2 sandwiches
    people_on_committee = 24  # There are 24 people on the committee
    croissants_per_package = 12  # Each package of croissants contains 12 mini croissants
    cost_per_package = 8.00  # Each package of croissants costs $8.00

    # Calculate the total number of croissants needed
    total_croissants = sandwiches_per_person * people_on_committee
    croissants_per_package = 12

    # Calculate the total number of packages of croissants needed
    total_packages = total_croissants / croissants_per_package

    # Calculate the total cost of the croissants
    total_cost = total_packages * cost_per_package
    result = total_cost
    return result

print(solution())