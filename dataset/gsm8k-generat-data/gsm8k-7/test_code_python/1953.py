def solution():
    price_per_model = 100
    num_kindergarten_models = 2
    num_elementary_models = 2 * num_kindergarten_models

    # Calculate the total number of models purchased
    total_models = num_kindergarten_models + num_elementary_models

    # Apply the 5% discount if the school bought more than 5 models
    if total_models > 5:
        discount = 0.05
        discounted_price_per_model = price_per_model * (1 - discount)
        total_cost = num_kindergarten_models * discounted_price_per_model + num_elementary_models * discounted_price_per_model
    else:
        total_cost = num_kindergarten_models * price_per_model + num_elementary_models * price_per_model

    result = total_cost
    return result

print(solution())