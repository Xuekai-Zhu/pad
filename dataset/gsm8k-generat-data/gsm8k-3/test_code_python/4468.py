def solution():
    """Owen bought 12 boxes of face masks that cost $9 per box. Each box has 50 pieces of masks. He repacked 6 of these boxes and sold them for $5 per 25 pieces. He sold the remaining 300 face masks in baggies at the rate of 10 pieces of mask for $3. How much profit did he make?"""
    
    # Calculate the cost of buying all the boxes of masks
    total_cost = 12 * 9

    # Calculate the number of masks in all the boxes
    total_masks = 12 * 50

    # Calculate the number of masks in the 6 boxes Owen repacked
    repacked_masks = 6 * 50

    # Calculate the number of sold masks in the repacked boxes
    sold_repacked_masks = (repacked_masks // 2) * 5

    # Calculate the number of remaining masks
    remaining_masks = total_masks - repacked_masks - (sold_repacked_masks * 2)

    # Calculate the profit from selling the remaining masks in baggies
    baggies_profit = (remaining_masks // 10) * 3

    # Calculate the total profit
    total_profit = baggies_profit + (sold_repacked_masks * 2) - total_cost

    # Display the total profit
    result = total_profit
    return result

print(solution())