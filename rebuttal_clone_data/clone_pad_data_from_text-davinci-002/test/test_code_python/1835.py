def solution():
    packs_of_stickers = 4
    stickers_per_pack = 30
    price_per_sticker = 0.1
    total_cost = packs_of_stickers * stickers_per_pack * price_per_sticker
    friend_share = total_cost / 2
    result = total_cost - friend_share
    return result

print(solution())