def solution():
    total_cost = 80  # Luigi spent $80 on 4 pizzas
    num_pizzas = 4
    pieces_per_pizza = 5
    total_pieces = num_pizzas * pieces_per_pizza

    # Calculate the cost per piece of pizza
    cost_per_piece = total_cost / total_pieces
    result = cost_per_piece
    return result

print(solution())