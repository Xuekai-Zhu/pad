def solution():
    previous_price = 0.45
    current_price = 0.50
    num_models = 30

    # Calculate Kirsty's budget with the previous price
    previous_budget = num_models * previous_price

    # Calculate how many models she can buy with the new price
    current_budget = previous_budget
    while current_budget >= current_price:
        num_models += 1
        current_budget = num_models * current_price

    # Subtract one since we went one model too far in the loop
    num_models -= 1
    result = num_models
    return result

print(solution())