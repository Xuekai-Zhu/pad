def solution():
    """Jangshe spent $610 on 7 pieces of clothing. One piece was $49 and another piece was $81. If the other pieces were all the same price, how many dollars was one of the other pieces?"""
    total_cost = 610
    piece_1_cost = 49
    piece_2_cost = 81
    num_pieces_without_piece_1_and_2 = 7 - 2
    remaining_cost = total_cost - piece_1_cost - piece_2_cost
    cost_per_piece = remaining_cost / num_pieces_without_piece_1_and_2
    result = cost_per_piece
    return result

print(solution())