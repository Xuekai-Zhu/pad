def solution():
    price_per_model = 100  # The price of one dinosaur model is $100
    num_models_k = 2  # The kindergarten library bought 2 models
    num_models_e = num_models_k * 2  # The elementary library bought twice as many as the kindergarten library
    total_models = num_models_k + num_models_e  # The total number of models the school bought
    if total_models > 5:  # If the school bought more than 5 models, there is a 5% reduction in price for each model
        price_per_model *= 0.95
    total_cost = (num_models_k + num_models_e) * price_per_model  # Calculate the total cost of all the models
    result = total_cost
    return result

print(solution())