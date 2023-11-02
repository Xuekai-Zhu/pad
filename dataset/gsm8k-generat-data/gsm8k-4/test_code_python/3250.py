def solution():
    """James splits 4 packs of stickers that have 30 stickers each. Each sticker cost $.10. If his friend pays for half how much did James pay?"""
    # Define the number of sticker packs and the cost per sticker
    PACKS = 4
    STICKERS_PER_PACK = 30
    STICKER_COST = 0.1

    # Calculate the total number of stickers
    total_stickers = PACKS * STICKERS_PER_PACK

    # Calculate the total cost of the stickers
    total_cost = total_stickers * STICKER_COST

    # Calculate how much James' friend paid
    friend_paid = total_cost / 2

    # Calculate how much James paid
    james_paid = total_cost - friend_paid

    # Return the result
    result = round(james_paid, 2)
    return result

print(solution())