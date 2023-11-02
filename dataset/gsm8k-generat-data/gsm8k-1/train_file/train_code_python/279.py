def solution():
    """The card shop has two boxes of cards. The first box contains cards that cost $1.25 each. The second box contains cards that cost $1.75 each. A boy then comes in and buys 6 cards from each box. What was the total cost, in dollars, of the cards he bought?"""
    cards_per_box = 6
    cost_box1 = 1.25
    cost_box2 = 1.75
    total_cost = (cards_per_box * cost_box1) + (cards_per_box * cost_box2)
    result = total_cost
    return result

print(solution())