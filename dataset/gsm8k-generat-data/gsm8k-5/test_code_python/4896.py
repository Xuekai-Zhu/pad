def solution():
    price_per_mask = 0.5  # Grover will sell each face mask for $0.50
    masks_per_box = 20  # Each box has 20 face masks
    total_boxes = 3  # Grover bought 3 boxes of face masks
    total_cost = 15  # Grover bought the 3 boxes for $15

    # Calculate the total revenue from selling the face masks
    total_revenue = price_per_mask * masks_per_box * total_boxes

    # Calculate the total profit from selling the face masks
    total_profit = total_revenue - total_cost
    result = total_profit
    return result

print(solution())