def solution():
    # Define the cost of one dinosaur model
    model_cost = 100

    # Calculate the number of models bought for the kindergarten library
    kinder_models = 2

    # Calculate the number of models bought for the elementary library
    elem_models = kinder_models * 2

    # Calculate the total number of models bought
    total_models = kinder_models + elem_models

    # Apply the 5% reduction in price for each model
    reduced_cost = model_cost - (model_cost * 0.05)

    # Calculate the total cost of all the models
    total_cost = total_models * reduced_cost
    result = total_cost
    return result

print(solution())