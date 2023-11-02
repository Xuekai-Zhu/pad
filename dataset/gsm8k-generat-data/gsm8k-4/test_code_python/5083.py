def solution():
    """An auctioneer raises the price of an item he is auctioning by $5 every time someone new bids on it. Two people enter a bidding war on a desk and the price goes from $15 to $65 before the desk is sold. How many times did each person bid on the desk?"""
    # Define the starting and final prices of the desk
    starting_price = 15
    final_price = 65

    # Define the bid increment
    bid_increment = 5

    # Calculate the number of times each person bid
    bidder1_bids = (final_price - starting_price) // (2 * bid_increment)
    bidder2_bids = bidder1_bids

    # Check if there was an odd number of bids and assign the additional bid to one of the bidders
    if (final_price - starting_price) % (2 * bid_increment) >= bid_increment:
        bidder1_bids += 1
    else:
        bidder2_bids += 1

    # return the result as a tuple
    result = (bidder1_bids, bidder2_bids)
    return result

print(solution())