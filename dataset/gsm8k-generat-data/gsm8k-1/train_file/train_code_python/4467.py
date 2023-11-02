def solution():
    """Owen bought 12 boxes of face masks that cost $9 per box. Each box has 50 pieces of masks. He repacked 6 of these boxes and sold them for $5 per 25 pieces. He sold the remaining 300 face masks in baggies at the rate of 10 pieces of mask for $3. How much profit did he make?"""
    num_boxes = 12
    cost_per_box = 9
    num_masks_per_box = 50
    repacked_boxes = 6
    repack_price = 5
    repacked_masks = repacked_boxes * num_masks_per_box
    repack_pieces_price = (repack_price / 25) * 10
    repack_profit = repack_pieces_price * repacked_masks
    remaining_masks = (num_boxes - repacked_boxes) * num_masks_per_box
    remaining_baggies = remaining_masks / 10
    baggies_price = 3
    remaining_profit = remaining_baggies * baggies_price
    total_profit = (repack_profit + remaining_profit) - (num_boxes * cost_per_box)
    result = total_profit
    return result

print(solution())