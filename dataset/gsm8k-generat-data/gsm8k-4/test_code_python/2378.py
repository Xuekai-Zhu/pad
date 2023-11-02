def solution():
    """Last week, Tony went to a toy store and bought $250 a set of Lego blocks, a $120 worth toy sword, and a $35 play dough. He bought 3 sets of lego, 7 toy swords, and 10 play doughs. How much did Tony pay in total?"""
    # Define the prices of each item and the number of items bought
    lego_price = 250
    sword_price = 120
    play_dough_price = 35
    lego_qty = 3
    sword_qty = 7
    play_dough_qty = 10

    # Calculate the total cost of each item type
    total_lego_cost = lego_price * lego_qty
    total_sword_cost = sword_price * sword_qty
    total_play_dough_cost = play_dough_price * play_dough_qty

    # Calculate the total cost of all items
    total_cost = total_lego_cost + total_sword_cost + total_play_dough_cost

    # return the result
    result = total_cost
    return result

print(solution())