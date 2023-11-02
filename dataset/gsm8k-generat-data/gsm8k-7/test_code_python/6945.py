def solution():
    num_packs = 3
    cost_per_piece = 0.10
    num_pieces_per_pack = 20

    # Calculate the total number of pieces of string cheese that Josh bought
    total_pieces = num_packs * num_pieces_per_pack

    # Calculate the total cost of all the string cheese
    total_cost = total_pieces * cost_per_piece
    result = total_cost
    return result

print(solution())