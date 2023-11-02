def solution():
    """The Science museum sells dinosaur models for $100 each. A certain school bought 2 models for the kindergarten library and also bought twice as many for the elementary library. Since the school bought more than 5 models, there was a 5% reduction in price for each model. How much did the school pay in all?"""
    cost_per_model = 100
    kindergarten_models = 2
    elementary_models = kindergarten_models * 2
    total_models = kindergarten_models + elementary_models
    
    if total_models > 5:
        cost_per_model *= 0.95
    
    total_cost = cost_per_model * total_models
    result = total_cost
    
    return result

print(solution())