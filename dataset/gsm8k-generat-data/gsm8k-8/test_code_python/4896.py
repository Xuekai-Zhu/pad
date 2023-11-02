def solution():
    # Define the variables
    boxes = 3
    masks_per_box = 20
    mask_price = 0.5
    total_cost = 15

    # Calculate the total number of masks
    total_masks = boxes * masks_per_box

    # Calculate the total revenue from selling the masks
    total_revenue = total_masks * mask_price

    # Calculate the profit
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())