def solution():
    """James gets 3 parking tickets. The first 2 cost $150 each and the third cost 1/3 as much as one of these. His roommate agrees to pay half the cost. How much money does he have left if he had $500 in the bank?"""
    ticket1_cost = 150
    ticket2_cost = 150
    ticket3_cost = ticket1_cost / 3
    total_cost = ticket1_cost + ticket2_cost + ticket3_cost
    james_share = total_cost / 2
    money_left = 500 - james_share
    result = money_left
    return result

print(solution())