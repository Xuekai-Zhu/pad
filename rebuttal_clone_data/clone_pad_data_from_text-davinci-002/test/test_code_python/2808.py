def solution():
    total_spent = 610
    piece_1 = 49
    piece_2 = 81
    remaining_pieces = total_spent - piece_1 - piece_2
    equal_piece_price = remaining_pieces / 5
    result = equal_piece_price
    return result

print(solution())