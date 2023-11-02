def solution():
    num_boxes = 3
    masks_per_box = 20
    mask_price = 0.5
    total_cost = 15

    # Calculate the total number of masks that Grover bought
    total_masks = num_boxes * masks_per_box

    # Calculate the total revenue from selling all masks
    total_revenue = total_masks * mask_price

    # Calculate Grover's profit
    total_profit = total_revenue - total_cost
    result = total_profit
    return result

print(solution())