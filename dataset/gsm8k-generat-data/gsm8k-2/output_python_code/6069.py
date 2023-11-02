def solution():
    """Luigi bought four pizzas for $80. Each pizza was cut into 5 pieces. How much did each piece of pizza cost, in dollars?"""
    total_cost = 80
    num_pizzas = 4
    num_pieces = num_pizzas * 5
    cost_per_piece = total_cost / num_pieces
    result = cost_per_piece
    return result

print(solution())