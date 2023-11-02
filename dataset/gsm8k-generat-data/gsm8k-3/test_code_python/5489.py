def solution():
    """Kirsty collects small models of animals. The last time she bought some, each one cost $0.45. She saves enough to buy 30 models, but when she goes to the shop, she finds out that the price had increased to $0.50. How many models can she buy now?"""
    # Define the original price and the new price
    ORIGINAL_PRICE = 0.45
    NEW_PRICE = 0.50

    # Determine how many models Kirsty can buy at the new price
    new_budget = 30 * NEW_PRICE
    new_num_models = int(new_budget / NEW_PRICE)

    # Determine how much Kirsty would have spent at the original price
    original_budget = 30 * ORIGINAL_PRICE

    # Determine how many models Kirsty can buy at the original price
    original_num_models = int(original_budget / ORIGINAL_PRICE)

    # Choose the maximum number of models Kirsty can buy
    max_num_models = max(new_num_models, original_num_models)

    # Display the maximum number of models Kirsty can buy
    result = max_num_models
    return result

print(solution())