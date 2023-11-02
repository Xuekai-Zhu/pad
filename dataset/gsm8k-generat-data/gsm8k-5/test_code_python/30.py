def solution():
    total_pizzas = 4 * 4  # Each person buys one personal pan pizza cut into 4 pieces
    bill_dale_eaten = 0.5 * 2 * 4  # Bill and Dale eat 50% of their pizzas
    ann_cate_eaten = 0.75 * 2 * 4  # Ann and Cate eat 75% of their pizzas

    # Calculate the total number of pizza pieces left uneaten
    pizza_pieces_left = total_pizzas - bill_dale_eaten - ann_cate_eaten
    result = pizza_pieces_left
    return result

print(solution())