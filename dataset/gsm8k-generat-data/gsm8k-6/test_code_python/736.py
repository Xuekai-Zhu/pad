def solution():
    # Calculate the cost of the samosas
    samosas_cost = 3 * 2

    # Calculate the cost of the pakoras
    pakoras_cost = 4 * 3

    # Calculate the total cost of the meal before tax
    total_cost = samosas_cost + pakoras_cost + 2

    # Calculate the cost of the tip
    tip = 0.25 * total_cost

    # Calculate the total cost of the meal with tax and tip
    total_cost_with_tax_and_tip = total_cost + tip

    result = total_cost_with_tax_and_tip
    return result

print(solution())