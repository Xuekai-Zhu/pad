def solution():
    current_value = 400000
    tax_rate = 0.02
    max_tax = 15000
    increase_percent = 0.25

    # Calculate the new value of the house after the improvement
    new_value = current_value * (1 + increase_percent)

    # Find the maximum allowed value for the house to keep the tax bill within budget
    max_value = (max_tax / tax_rate) / 12

    # Calculate the maximum amount that can be spent on improvements
    max_improvement_cost = max_value - current_value

    # Return the result
    result = max_improvement_cost
    return result

print(solution())