def solution():
    # Define the initial variables
    tax_rate = 0.02
    current_value = 400000
    increase_percent = 0.25
    max_tax_amount = 15000

    # Calculate the new value of the house
    new_value = current_value * (1 + increase_percent)

    # Calculate the maximum allowed value of improvements
    max_improvement_value = (max_tax_amount / tax_rate) - new_value

    result = max_improvement_value
    return result

print(solution())