def solution():
    """The Science museum sells dinosaur models for $100 each. A certain school bought 2 models for the kindergarten library and also bought twice as many for the elementary library. Since the school bought more than 5 models, there was a 5% reduction in price for each model. How much did the school pay in all?"""
    # Define the cost of each dinosaur model
    MODEL_PRICE = 100

    # Calculate the number of models bought for the kindergarten library
    k_library = 2

    # Calculate the number of models bought for the elementary library
    e_library = k_library * 2

    # Calculate the total number of models bought
    total_models = k_library + e_library

    # Calculate the discounted price per model
    if total_models > 5:
        discount = 0.05
    else:
        discount = 0
    discounted_price = MODEL_PRICE - (MODEL_PRICE * discount)

    # Calculate the total cost of all the models
    total_cost = (k_library + e_library) * discounted_price

    # Display the total cost
    result = total_cost
    return result

print(solution())