def solution():
    quantity_per_pack = 1  # in cups
    cost_per_pack = 2.0
    cups_per_day = 0.5
    num_days = 30

    # Calculate total cups required for 30 days
    total_cups_required = cups_per_day * num_days

    # Calculate total packs required to meet the required cups
    total_packs_required = total_cups_required / quantity_per_pack

    # Calculate the total cost of all packs required
    total_cost = total_packs_required * cost_per_pack
    result = total_cost
    return result

print(solution())