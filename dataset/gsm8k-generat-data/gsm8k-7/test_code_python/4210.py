def solution():
    num_people = 24
    sandwiches_per_person = 2
    croissants_per_package = 12
    cost_per_package = 8.0

    # Calculate the total number of croissants needed
    total_croissants = num_people * sandwiches_per_person

    # Calculate the total number of packages needed
    total_packages = total_croissants / croissants_per_package

    # Calculate the total cost of all croissants needed
    total_cost = total_packages * cost_per_package
    result = total_cost
    return result

print(solution())