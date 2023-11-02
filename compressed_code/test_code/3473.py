def solution():
    
    boxes_bought = 12
    cost_per_box = 9
    pieces_per_box = 50
    total_masks = boxes_bought * pieces_per_box
    masks_repacked = 6 * pieces_per_box
    masks_remaining = total_masks - masks_repacked
    masks_repacked_sold = (masks_repacked // 25) * 5
    masks_remaining_sold = (masks_remaining // 10) * 3
    total_profit = (masks_repacked_sold + masks_remaining_sold) - (boxes_bought * cost_per_box)
    result = total_profit
    return result

print(solution())