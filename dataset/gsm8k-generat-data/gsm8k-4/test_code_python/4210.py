def solution():
    """For the gala luncheon planning committee, Margaret wants to serve chicken salad sandwiches using mini croissants. She wants there to be enough food that each person on the committee can have 2 sandwiches each. Her bakery offers 12 minis croissants for $8.00. There are 24 people on the committee. How much will she spend on croissants?"""
    # Define the number of croissants needed
    croissants_needed = 2 * 24

    # Define the number of croissants per package and the cost per package
    croissants_per_package = 12
    cost_per_package = 8.00

    # Calculate the number of packages needed
    packages_needed = croissants_needed / croissants_per_package

    # Calculate the total cost of the croissants
    total_cost = packages_needed * cost_per_package

    # Return the result
    result = total_cost
    return result

print(solution())