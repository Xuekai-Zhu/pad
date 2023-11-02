def solution():
    """Owen bought 12 boxes of face masks that cost $9 per box. Each box has 50 pieces of masks. He repacked 6 of these boxes and sold them for $5 per 25 pieces. He sold the remaining 300 face masks in baggies at the rate of 10 pieces of mask for $3. How much profit did he make?"""
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