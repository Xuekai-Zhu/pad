def solution():
    """GiGi took out a big bowl of mushrooms from the refrigerator. She cut each mushroom into 4 pieces. Her twins, Kenny and Karla sprinkled mushrooms on their pizzas and baked them in the oven. Kenny grabbed a handful and sprinkled 38 mushroom pieces on his pizza. Karla scooped them up with both hands and sprinkled 42 mushroom pieces on her pizza. On the cutting board, were 8 pieces of mushrooms remaining. How many mushrooms did GiGi cut up at the beginning?"""
    mushroom_pieces = 38 + 42 + 8
    mushrooms_cut = mushroom_pieces / 4
    result = mushrooms_cut
    return result

print(solution())