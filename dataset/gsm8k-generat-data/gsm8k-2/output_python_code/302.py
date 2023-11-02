def solution():
    """Tommy is making 12 loaves of bread. He needs 4 pounds of flour per loaf. A 10-pound bag of flour costs $10 and a 12-pound bag costs $13. When he is done making his bread, he has no use for flour and so he will throw away whatever is left. How much does he spend on flour if he buys the cheapest flour to get enough?"""
    total_flour_needed = 12 * 4
    cheapest_price_per_pound = min(10/10, 13/12)
    total_cost = cheapest_price_per_pound * total_flour_needed
    result = total_cost
    return result

print(solution())