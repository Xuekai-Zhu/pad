def solution():
    """James splits 4 packs of stickers that have 30 stickers each. Each sticker cost $.10. If his friend pays for half how much did James pay?"""
    packs = 4
    stickers_per_pack = 30
    sticker_cost = 0.1
    total_stickers = packs * stickers_per_pack
    total_cost = total_stickers * sticker_cost
    friend_cost = total_cost / 2
    james_cost = total_cost - friend_cost
    result = james_cost
    return result

print(solution())