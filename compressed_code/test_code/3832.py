def solution():
    
    total_cost = 610
    piece_1_cost = 49
    piece_2_cost = 81
    num_pieces_without_piece_1_and_2 = 7 - 2
    remaining_cost = total_cost - piece_1_cost - piece_2_cost
    cost_per_piece = remaining_cost / num_pieces_without_piece_1_and_2
    result = cost_per_piece
    return result

print(solution())