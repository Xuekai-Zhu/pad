def solution():
    # Calculate the total number of stickers and the total cost of stickers for James
    total_stickers = 4 * 30  # 4 packs of stickers with 30 stickers each
    total_cost = total_stickers * 0.10  # each sticker costs $.10

    # Calculate the amount that James' friend needs to pay
    friend_payment = total_cost/2

    # Calculate the amount that James needs to pay
    james_payment = total_cost - friend_payment
    result = james_payment
    return result

print(solution())