def solution():
    # Calculate the total cost of the three puppies on sale
    sale_puppies_cost = 3 * 150  

    # Calculate the cost of the two other puppies
    other_puppies_cost = 800 - sale_puppies_cost  
    num_other_puppies = 2  
    cost_per_other_puppy = other_puppies_cost / num_other_puppies

    result = cost_per_other_puppy
    return result

print(solution())