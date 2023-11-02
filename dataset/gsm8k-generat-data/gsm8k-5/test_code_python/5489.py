def solution():
    original_price = 0.45  # The original price of each model
    new_price = 0.50  # The new price of each model
    total_budget = 30 * original_price  # Kirsty's total budget
    max_models = total_budget // new_price  # The maximum number of models she can buy with the new price
    result = max_models
    return result

print(solution())