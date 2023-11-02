def solution():
    """GiGi took out a big bowl of mushrooms from the refrigerator. She cut each mushroom into 4 pieces. Her twins, Kenny and Karla sprinkled mushrooms on their pizzas and baked them in the oven. Kenny grabbed a handful and sprinkled 38 mushroom pieces on his pizza. Karla scooped them up with both hands and sprinkled 42 mushroom pieces on her pizza. On the cutting board, were 8 pieces of mushrooms remaining. How many mushrooms did GiGi cut up at the beginning?"""
    kenny_pieces = 38
    karla_pieces = 42
    remaining_pieces = 8
    total_pieces = kenny_pieces + karla_pieces + remaining_pieces
    total_mushrooms = total_pieces // 4
    result = total_mushrooms
    return result

print(solution())