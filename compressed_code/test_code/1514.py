def solution():
    
    model_price = 100
    total_models = 2 + 2*2 
    if total_models > 5:
        model_price = model_price * 0.95
    total_price = total_models * model_price
    result = total_price
    return result

print(solution())