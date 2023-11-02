def solution():
    """Arven bought five puppies for a total cost of $800. Three puppies are on sale for $150 each. How much does each of those two other puppies cost if they cost the same?"""
    sale_price = 150
    sale_puppies_total = 3 * sale_price
    remaining_cost = 800 - sale_puppies_total
    remaining_puppies = 5 - 3
    price_per_puppy = remaining_cost / remaining_puppies
    result = price_per_puppy
    return result

print(solution())