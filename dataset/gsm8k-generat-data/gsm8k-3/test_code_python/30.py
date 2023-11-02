def solution():
    """Ann, Bill, Cate, and Dale each buy personal pan pizzas cut into 4 pieces. If Bill and Dale eat 50% of their pizzas and Ann and Cate eat 75% of the pizzas, how many pizza pieces are left uneaten?"""
    # Define the total number of pizzas and the number of pieces per pizza
    total_pizzas = 4
    pieces_per_pizza = 4

    # Calculate the total number of pizza pieces
    total_pieces = total_pizzas * pieces_per_pizza

    # Calculate the number of pieces eaten by Bill and Dale
    bd_pieces = total_pizzas * 0.5 * pieces_per_pizza

    # Calculate the number of pieces eaten by Ann and Cate
    ac_pieces = total_pizzas * 0.75 * pieces_per_pizza

    # Calculate the number of uneaten pizza pieces
    uneaten_pieces = total_pieces - bd_pieces - ac_pieces

    # return the result
    result = uneaten_pieces
    return result

print(solution())