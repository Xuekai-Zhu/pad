def solution():
    """Kirsty collects small models of animals. The last time she bought some, each one cost $0.45. She saves enough to buy 30 models, but when she goes to the shop, she finds out that the price had increased to $0.50. How many models can she buy now?"""
    previous_price = 0.45
    current_price = 0.50
    budget = 30 * previous_price
    new_price_models = budget / current_price
    result = int(new_price_models)
    return result

print(solution())