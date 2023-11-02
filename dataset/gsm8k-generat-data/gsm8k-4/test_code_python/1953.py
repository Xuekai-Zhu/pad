def solution():
    """The Science museum sells dinosaur models for $100 each. A certain school bought 2 models for the kindergarten library and also bought twice as many for the elementary library. Since the school bought more than 5 models, there was a 5% reduction in price for each model. How much did the school pay in all?"""
    # Define the price per dinosaur model and the number of models bought
    PRICE_PER_MODEL = 100
    num_kindergarten_models = 2
    num_elementary_models = 2*num_kindergarten_models

    # Calculate the total number of models bought
    total_models = num_kindergarten_models + num_elementary_models

    # Apply the discount if the school bought more than 5 models
    if total_models > 5:
        PRICE_PER_MODEL = PRICE_PER_MODEL * 0.95

    # Calculate the total cost of the models
    total_cost = (num_kindergarten_models + num_elementary_models) * PRICE_PER_MODEL

    # return the result
    result = total_cost
    return result

print(solution())