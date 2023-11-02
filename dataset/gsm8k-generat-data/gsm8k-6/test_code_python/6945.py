def solution():
    # Calculate the total cost of the string cheese
    packs = 3
    cost_per_piece = 10/100  # 10 cents is 1/10 of a dollar
    pieces_per_pack = 20
    total_pieces = packs * pieces_per_pack
    total_cost = total_pieces * cost_per_piece
    result = total_cost
    return result

print(solution())