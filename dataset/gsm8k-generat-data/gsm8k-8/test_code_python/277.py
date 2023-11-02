def solution():
    # Calculate the total cost of the three puppies on sale
    sale_puppies_cost = 3 * 150

    # Calculate the cost of the two other puppies
    other_puppies_cost = 800 - sale_puppies_cost

    # Calculate the cost of each of the two other puppies
    cost_each_other_puppy = other_puppies_cost / 2
    result = cost_each_other_puppy
    return result

print(solution())