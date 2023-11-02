def solution():
    packs_of_stickers = 4  # James splits 4 packs of stickers
    stickers_per_pack = 30  # Each pack has 30 stickers
    sticker_cost = 0.1  # Each sticker costs $.10

    # Calculate the total cost of the stickers
    total_cost = packs_of_stickers * stickers_per_pack * sticker_cost

    # Calculate how much James's friend paid
    friend_payment = total_cost / 2

    # Calculate how much James paid
    james_payment = total_cost - friend_payment
    result = james_payment
    return result

print(solution())