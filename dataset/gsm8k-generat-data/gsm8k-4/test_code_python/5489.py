def solution():
    """Kirsty collects small models of animals. The last time she bought some, each one cost $0.45. She saves enough to buy 30 models, but when she goes to the shop, she finds out that the price had increased to $0.50. How many models can she buy now?"""
    # Define the initial price per model and the number of models Kirsty can afford
    INITIAL_PRICE = 0.45
    MAX_MODELS = 30

    # Calculate the amount of money Kirsty has saved
    total_money = INITIAL_PRICE * MAX_MODELS

    # Define the new price per model
    NEW_PRICE = 0.50

    # Calculate the maximum number of models Kirsty can buy at the new price
    max_models = total_money / NEW_PRICE

    result = int(max_models)
    return result

print(solution())