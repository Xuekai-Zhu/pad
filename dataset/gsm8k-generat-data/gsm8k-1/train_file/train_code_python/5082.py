def solution():
    """An auctioneer raises the price of an item he is auctioning by $5 every time someone new bids on it. Two people enter a bidding war on a desk and the price goes from $15 to $65 before the desk is sold. How many times did each person bid on the desk?"""
    initial_price = 15
    final_price = 65
    price_increase = 5
    bids = (final_price - initial_price) / price_increase
    person1_bids = bids / 2
    person2_bids = bids / 2
    result = (person1_bids, person2_bids)
    return result

print(solution())