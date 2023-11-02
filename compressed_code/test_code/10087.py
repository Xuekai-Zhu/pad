def solution():
    
    previous_price = 0.45
    current_price = 0.50
    budget = 30 * previous_price
    new_price_models = budget / current_price
    result = int(new_price_models)
    return result

print(solution())