def solution():
    packs = 3  # Josh buys 3 packs of string cheese
    cost_per_piece = 0.10  # Each piece of string cheese costs 10 cents
    pieces_per_pack = 20  # Each pack has 20 string cheeses in them

    # Calculate the total cost
    total_cost = packs * pieces_per_pack * cost_per_piece
    result = total_cost
    return result

print(solution())