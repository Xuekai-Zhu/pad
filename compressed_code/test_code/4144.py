def solution():
    
    pepperoni_pieces = 30
    ham_pieces = 2 * pepperoni_pieces
    sausage_pieces = pepperoni_pieces + 12
    total_meat_pieces = pepperoni_pieces + ham_pieces + sausage_pieces
    pieces_per_slice = total_meat_pieces / 6
    result = pieces_per_slice
    return result

print(solution())