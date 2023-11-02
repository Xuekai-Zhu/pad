def solution():
    """Last week, Tony went to a toy store and bought $250 a set of Lego blocks, a $120 worth toy sword, and a $35 play dough. He bought 3 sets of lego, 7 toy swords, and 10 play doughs. How much did Tony pay in total?"""
    lego_price = 250
    sword_price = 120
    dough_price = 35
    total_lego_price = lego_price * 3
    total_sword_price = sword_price * 7
    total_dough_price = dough_price * 10
    total_price = total_lego_price + total_sword_price + total_dough_price
    result = total_price
    return result

print(solution())