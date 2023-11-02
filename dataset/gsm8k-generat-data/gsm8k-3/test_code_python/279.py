def solution():
    """Arven bought five puppies for a total cost of $800. Three puppies are on sale for $150 each. How much does each of those two other puppies cost if they cost the same?"""
    # Calculate the total cost of the three puppies on sale
    sale_cost = 3 * 150

    # Calculate the cost of the two other puppies
    other_cost = 800 - sale_cost
    other_count = 5 - 3
    other_puppy_cost = other_cost / other_count

    # Display the cost of each of the two other puppies
    result = other_puppy_cost
    return result

print(solution())