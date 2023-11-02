def solution():
    """The card shop has two boxes of cards. The first box contains cards that cost $1.25 each. The second box contains cards that cost $1.75 each. A boy then comes in and buys 6 cards from each box. What was the total cost, in dollars, of the cards he bought?"""
    box1_price = 1.25
    box2_price = 1.75
    cards_per_box = 6
    total_cost = (box1_price * cards_per_box) + (box2_price * cards_per_box)
    result = total_cost
    return result

print(solution())