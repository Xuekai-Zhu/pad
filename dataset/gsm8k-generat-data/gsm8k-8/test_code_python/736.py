def solution():
    # Calculate the total cost of samosas
    samosa_cost = 3 * 2

    # Calculate the total cost of pakoras
    pakora_cost = 4 * 3

    # Calculate the total cost without tax
    total_cost_without_tax = samosa_cost + pakora_cost + 2

    # Calculate the tip amount
    tip = 0.25 * total_cost_without_tax

    # Calculate the total cost with tax and tip
    total_cost_with_tax_and_tip = total_cost_without_tax + tip

    result = total_cost_with_tax_and_tip
    return result

print(solution())