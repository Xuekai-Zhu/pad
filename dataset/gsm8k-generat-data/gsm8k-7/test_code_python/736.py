def solution():
    samosa_price = 2
    num_samosas = 3

    pakora_price = 3
    num_pakoras = 4

    lassi_price = 2
    tip_percent = 0.25 # 25% tip

    # Calculate the total cost of samosas
    samosas_cost = samosa_price * num_samosas

    # Calculate the total cost of pakoras
    pakoras_cost = pakora_price * num_pakoras

    # Calculate the total cost of the meal before tip and tax
    total_cost_before_tip_tax = samosas_cost + pakoras_cost + lassi_price

    # Calculate the tip
    tip = total_cost_before_tip_tax * tip_percent

    # Calculate the total cost of the meal with tip
    total_cost_with_tip = total_cost_before_tip_tax + tip

    # Calculate the cost with tax (assumed to be 7.5%)
    tax_percent = 0.075
    cost_with_tax = total_cost_with_tip * (1 + tax_percent)

    result = cost_with_tax
    return result

print(solution())