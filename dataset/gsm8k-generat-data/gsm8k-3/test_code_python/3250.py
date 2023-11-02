def solution():
    """James splits 4 packs of stickers that have 30 stickers each. Each sticker cost $.10. If his friend pays for half how much did James pay?"""
    # Define the number of sticker packs and stickers in each pack
    STICKER_PACKS = 4
    STICKERS_PER_PACK = 30

    # Define the cost per sticker
    COST_PER_STICKER = 0.10

    # Calculate the total number of stickers
    total_stickers = STICKER_PACKS * STICKERS_PER_PACK

    # Calculate the total cost of all the stickers
    total_cost = total_stickers * COST_PER_STICKER

    # Calculate the cost that James paid
    james_paid = total_cost / 2

    # Display the cost that James paid
    result = james_paid
    return result

print(solution())