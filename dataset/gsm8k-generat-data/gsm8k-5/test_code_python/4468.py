def solution():
    # Cost of 12 boxes of face masks
    cost = 12 * 9

    # Total number of masks in 12 boxes
    total_masks = 12 * 50

    # Number of masks in 6 repacked boxes
    repacked_masks = 6 * 50

    # Number of masks sold in bags
    bagged_masks = total_masks - repacked_masks

    # Cost of making repacked boxes
    repack_cost = 6 * 9 / 2  # 6 boxes at $9 per box, divided by 2 (since each repacked box has 25 masks)

    # Revenue from selling repacked boxes
    repack_revenue = 6 * 5 * 2  # 6 boxes sold at $5 per 25 masks, multiplied by 2 (since each repacked box has 25 masks)

    # Revenue from selling bagged masks
    bagged_revenue = (bagged_masks / 10) * 3

    # Total profit
    profit = repack_revenue + bagged_revenue - cost - repack_cost
    result = profit
    return result

print(solution())