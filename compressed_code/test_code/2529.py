def solution():
    
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