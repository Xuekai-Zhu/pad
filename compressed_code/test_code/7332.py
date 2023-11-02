def solution():
    
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