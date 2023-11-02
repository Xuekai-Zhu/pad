def solution():
    """An auctioneer raises the price of an item he is auctioning by $5 every time someone new bids on it. Two people enter a bidding war on a desk and the price goes from $15 to $65 before the desk is sold. How many times did each person bid on the desk?"""
    starting_price = 15
    final_price = 65
    bid_increase = 5
    total_bids = (final_price - starting_price) // 5
    person1_bids = (total_bids + 1) // 2
    person2_bids = total_bids - person1_bids
    result = (person1_bids, person2_bids)
    return result

print(solution())