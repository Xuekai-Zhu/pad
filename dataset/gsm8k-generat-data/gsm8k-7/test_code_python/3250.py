def solution():
    num_packs = 4
    stickers_per_pack = 30
    sticker_cost = 0.1

    # Calculate the total number of stickers in all packs
    total_stickers = num_packs * stickers_per_pack

    # Calculate the total cost of all stickers
    total_cost = total_stickers * sticker_cost

    # Calculate the amount James paid (half the total cost)
    james_paid = total_cost / 2
    result = james_paid
    return result

print(solution())