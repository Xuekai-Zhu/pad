def solution():
    """Rory makes a cake that weighs 20 ounces. She cuts into 8 pieces. Rory and her mom each have a piece. How much does the remaining cake weigh?"""
    weight_of_cake = 20
    number_of_pieces = 8
    weight_of_one_piece = weight_of_cake / number_of_pieces
    pieces_eaten = 2
    remaining_pieces = number_of_pieces - pieces_eaten
    remaining_cake_weight = remaining_pieces * weight_of_one_piece
    result = remaining_cake_weight
    return result

print(solution())