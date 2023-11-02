def solution():
    """Arven bought five puppies for a total cost of $800. Three puppies are on sale for $150 each. How much does each of those two other puppies cost if they cost the same?"""
    # Define the total cost of the five puppies and the cost of the three on sale
    total_cost = 800
    sale_cost = 3 * 150

    # Calculate the cost of the two other puppies
    other_cost = total_cost - sale_cost
    other_cost_per_puppy = other_cost / 2

    # Return the result
    result = other_cost_per_puppy
    return result

print(solution())