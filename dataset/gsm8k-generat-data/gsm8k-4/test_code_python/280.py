def solution():
    """The card shop has two boxes of cards. The first box contains cards that cost $1.25 each. The second box contains cards that cost $1.75 each. A boy then comes in and buys 6 cards from each box. What was the total cost, in dollars, of the cards he bought?"""
    # Define the price of cards in each box and the number of cards bought from each box
    BOX_1_PRICE = 1.25
    BOX_2_PRICE = 1.75
    CARDS_PER_BOX = 6

    # Calculate the total cost of the cards bought
    total_cost = (BOX_1_PRICE * CARDS_PER_BOX) + (BOX_2_PRICE * CARDS_PER_BOX)

    # return the result
    result = total_cost
    return result

print(solution())