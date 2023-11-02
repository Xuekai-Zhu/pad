def solution():
    """Last week, Tony went to a toy store and bought $250 a set of Lego blocks, a $120 worth toy sword, and a $35 play dough. He bought 3 sets of lego, 7 toy swords, and 10 play doughs. How much did Tony pay in total?"""
    # Define the prices of each item
    LEGOS_PRICE = 250
    TOY_SWORD_PRICE = 120
    PLAY_DOUGH_PRICE = 35

    # Define the quantities of each item purchased
    legos_qty = 3
    toy_swords_qty = 7
    play_dough_qty = 10

    # Calculate the total cost of the legos
    legos_cost = legos_qty * LEGOS_PRICE

    # Calculate the total cost of the toy swords
    toy_swords_cost = toy_swords_qty * TOY_SWORD_PRICE

    # Calculate the total cost of the play doughs
    play_dough_cost = play_dough_qty * PLAY_DOUGH_PRICE

    # Calculate the total cost of all the items
    total_cost = legos_cost + toy_swords_cost + play_dough_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())