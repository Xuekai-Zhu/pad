def solution():
    
    masks_per_box = 20
    total_masks = masks_per_box * 3
    cost = 15
    price_per_mask = 0.5
    total_income = price_per_mask * total_masks
    profit = total_income - cost
    result = profit
    return result

print(solution())