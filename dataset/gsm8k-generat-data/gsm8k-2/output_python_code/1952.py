def solution():
    """The Science museum sells dinosaur models for $100 each. A certain school bought 2 models for the kindergarten library and also bought twice as many for the elementary library. Since the school bought more than 5 models, there was a 5% reduction in price for each model. How much did the school pay in all?"""
    model_price = 100
    total_models = 2 + 2*2 # 2 for kindergarten and twice as many for elementary
    if total_models > 5:
        model_price = model_price * 0.95
    total_price = total_models * model_price
    result = total_price
    return result

print(solution())