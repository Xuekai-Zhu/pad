def solution():
    """A man owned 1/2 of a lot. He sold 1/10 of his share for the amount of $460. What is the worth of the entire lot?"""
    man_share = 1/2
    sold_share = 1/10 * man_share
    sold_price = 460
    remaining_share = man_share - sold_share
    total_worth = remaining_share / sold_share * sold_price
    result = total_worth
    return result

print(solution())