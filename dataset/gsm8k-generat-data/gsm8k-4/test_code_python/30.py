def solution():
    """Ann, Bill, Cate, and Dale each buy personal pan pizzas cut into 4 pieces. If Bill and Dale eat 50% of their pizzas and Ann and Cate eat 75% of the pizzas, how many pizza pieces are left uneaten?"""
    # Define the number of pizzas and pieces per pizza
    num_pizzas = 4
    pieces_per_pizza = 4

    # Calculate the total number of pizza pieces
    total_pieces = num_pizzas * pieces_per_pizza

    # Calculate the number of pieces eaten by Bill and Dale
    bd_eaten = num_pizzas * 2 * 0.5

    # Calculate the number of pieces eaten by Ann and Cate
    ac_eaten = num_pizzas * 2 * 0.75

    # Calculate the number of pieces left uneaten
    pieces_uneaten = total_pieces - bd_eaten - ac_eaten

    # return the result
    result = pieces_uneaten
    return result

print(solution())