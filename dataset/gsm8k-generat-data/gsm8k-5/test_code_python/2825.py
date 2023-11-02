def solution():
    man_share = 1/2  # The man owned 1/2 of the lot
    sold_share = 1/10 * man_share  # He sold 1/10 of his share
    sold_share_price = 460  # He sold the share for $460

    # Calculate the worth of his original share
    original_share_price = sold_share_price / sold_share

    # Calculate the worth of the entire lot
    total_lot_worth = original_share_price / man_share
    result = total_lot_worth
    return result

print(solution())