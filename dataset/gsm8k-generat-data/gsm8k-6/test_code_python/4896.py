def solution():
    # Calculate Grover's cost for buying the face masks
    cost = 15  # Grover bought 3 boxes for $15
    masks_per_box = 20  # Each box has 20 face masks
    total_masks = 3 * masks_per_box  # Total face masks bought
    cost_per_mask = cost / total_masks  # Cost per mask

    # Calculate Grover's revenue from selling the face masks
    price_per_mask = 0.5  # Grover plans to sell each mask for $0.50
    total_revenue = total_masks * price_per_mask  # Total revenue

    # Calculate Grover's total profit
    total_profit = total_revenue - cost
    result = total_profit
    return result

print(solution())