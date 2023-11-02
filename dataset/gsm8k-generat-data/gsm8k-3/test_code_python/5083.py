def solution():
    """An auctioneer raises the price of an item he is auctioning by $5 every time someone new bids on it. Two people enter a bidding war on a desk and the price goes from $15 to $65 before the desk is sold. How many times did each person bid on the desk?"""
    # Define the starting price, final price, and bid increment
    START_PRICE = 15
    FINAL_PRICE = 65
    BID_INCREMENT = 5

    # Calculate the number of bids made by each person
    person_1_bids = (FINAL_PRICE - START_PRICE) // (2 * BID_INCREMENT)
    person_2_bids = person_1_bids + 1

    # Display the number of bids made by each person
    result = (person_1_bids, person_2_bids)
    return result

print(solution())