def solution():
    """Last week, Tony went to a toy store and bought $250 a set of Lego blocks, a $120 worth toy sword, and a $35 play dough. He bought 3 sets of lego, 7 toy swords, and 10 play doughs. How much did Tony pay in total?"""
    lego_cost = 250
    sword_cost = 120
    playdough_cost = 35
    lego_num = 3
    sword_num = 7
    playdough_num = 10
    total_cost = (lego_cost * lego_num) + (sword_cost * sword_num) + (playdough_cost * playdough_num)
    result = total_cost
    return result

print(solution())