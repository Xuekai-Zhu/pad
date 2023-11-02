def solution():
    """Arven bought five puppies for a total cost of $800. Three puppies are on sale for $150 each. How much does each of those two other puppies cost if they cost the same?"""
    total_cost = 800
    sale_puppy_cost = 150
    num_sale_puppies = 3
    num_other_puppies = 2
    cost_of_other_puppies = (total_cost - (sale_puppy_cost * num_sale_puppies)) / num_other_puppies
    result = cost_of_other_puppies
    return result

print(solution())