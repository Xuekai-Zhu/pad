def solution():
    # Calculate the total number of models bought
    total_models = 2 + 2*2  # 2 models for kindergarten, twice as many for elementary (4 models)
    
    # Check if there was a 5% reduction in price
    if total_models > 5:
        price_per_model = 100 * 0.95  # apply 5% reduction in price
    else:
        price_per_model = 100
        
    # Calculate the total cost of all the models
    total_cost = price_per_model * total_models
    result = total_cost
    return result

print(solution())