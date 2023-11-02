def solution():
    """The card shop has two boxes of cards. The first box contains cards that cost $1.25 each. The second box contains cards that cost $1.75 each. A boy then comes in and buys 6 cards from each box. What was the total cost, in dollars, of the cards he bought?"""
    # Define the cost of each card in dollars
    BOX1_PRICE = 1.25
    BOX2_PRICE = 1.75

    # Define the number of cards purchased from each box
    cards_per_box = 6

    # Calculate the total cost of the cards purchased
    box1_cost = cards_per_box * BOX1_PRICE
    box2_cost = cards_per_box * BOX2_PRICE
    total_cost = box1_cost + box2_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())