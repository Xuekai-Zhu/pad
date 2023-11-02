def solution():
    """GiGi took out a big bowl of mushrooms from the refrigerator. She cut each mushroom into 4 pieces. Her twins, Kenny and Karla sprinkled mushrooms on their pizzas and baked them in the oven. Kenny grabbed a handful and sprinkled 38 mushroom pieces on his pizza. Karla scooped them up with both hands and sprinkled 42 mushroom pieces on her pizza. On the cutting board, were 8 pieces of mushrooms remaining. How many mushrooms did GiGi cut up at the beginning?"""
    
    # Define the number of mushroom pieces left on the cutting board
    remaining_pieces = 8
    
    # Calculate the total number of mushroom pieces used on both pizzas
    total_pieces_on_pizzas = 38 + 42
    
    # Calculate the total number of mushroom pieces
    total_pieces = remaining_pieces + total_pieces_on_pizzas
    
    # Calculate the number of mushrooms that GiGi originally cut up
    original_mushrooms = total_pieces / 4
    
    result = original_mushrooms
    return result

print(solution())