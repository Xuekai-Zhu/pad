def solution():
    """A man owned 1/2 of a lot. He sold 1/10 of his share for the amount of $460. What is the worth of the entire lot?"""
    half_of_lot = 1/2
    sold_share = 1/10 * half_of_lot
    sold_share_price = 460
    sold_share_value = sold_share_price / sold_share
    lot_worth = sold_share_value / half_of_lot
    result = lot_worth
    return result

print(solution())