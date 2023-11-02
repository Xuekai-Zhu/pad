def solution():
    # Calculate the total cost of the three puppies on sale
    sale_puppies_cost = 3 * 150  # Three puppies cost $150 each
    # Calculate the cost of the other two puppies
    other_puppies_cost = 800 - sale_puppies_cost
    # Calculate the cost of each of the other two puppies
    cost_per_puppy = other_puppies_cost / 2
    result = cost_per_puppy
    return result

print(solution())