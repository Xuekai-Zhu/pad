def solution():
    # Calculate the total cost of the 12 boxes of face masks
    total_cost = 12 * 9

    # Calculate the total number of face masks in the 12 boxes
    total_masks = 12 * 50

    # Calculate the number of repacked masks and the total profit from selling them
    repacked_masks = 6 * 50
    repacked_profit = (repacked_masks / 25) * 5 - (6 * 9)

    # Calculate the number of masks sold in baggies and the total profit from selling them
    baggies_masks = total_masks - repacked_masks
    baggies_profit = (baggies_masks / 10) * 3 - (total_cost - (6 * 9))

    # Calculate the total profit
    total_profit = repacked_profit + baggies_profit

    result = total_profit
    return result

print(solution())