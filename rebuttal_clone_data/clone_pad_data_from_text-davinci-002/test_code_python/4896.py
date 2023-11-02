def solution():
    boxes_bought = 3
    masks_per_box = 20
    price_per_mask = 0.50
    total_masks = boxes_bought * masks_per_box
    total_profit = total_masks * price_per_mask
    return total_profit

print(solution())