def solution():
    """GiGi took out a big bowl of mushrooms from the refrigerator.  She cut each mushroom into 4 pieces.  Her twins, Kenny and Karla sprinkled mushrooms on their pizzas and baked them in the oven.  Kenny grabbed a handful and sprinkled 38 mushroom pieces on his pizza.  Karla scooped them up with both hands and sprinkled 42 mushroom pieces on her pizza.  On the cutting board, were 8 pieces of mushrooms remaining.  How many mushrooms did GiGi cut up at the beginning?"""
    # Calculate the total number of mushroom pieces used by Kenny and Karla
    total_pieces_used = 38 + 42

    # Calculate the total number of mushrooms cut up by GiGi at the beginning
    total_pieces_at_beginning = total_pieces_used + 8

    # Calculate the total number of mushrooms cut up at the beginning
    mushrooms_at_beginning = total_pieces_at_beginning / 4

    # Display the total number of mushrooms cut up at the beginning
    result = mushrooms_at_beginning
    return result

print(solution())