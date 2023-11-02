def solution():
    """Carmen goes to an auction to win an antique desk. She accepts the opening bid of $200 and continues bidding until she wins. The bids on the desk rise by $50 each time and 3 other people each bid once. Carmen bids after each of the 3 other people and eventually wins. How much money, in dollars, does the desk cost her?"""
    opening_bid = 200
    bid_increase = 50
    num_bids = 3
    total_bids = num_bids * bid_increase
    winning_bid = opening_bid + total_bids
    total_cost = winning_bid + total_bids
    result = total_cost
    return result

print(solution())