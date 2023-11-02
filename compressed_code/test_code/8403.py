def solution():
    
    pieces_per_birdhouse = 7
    cost_per_piece = 1.5
    profit_per_birdhouse = 5.5
    total_cost = pieces_per_birdhouse * cost_per_piece
    selling_price = total_cost + profit_per_birdhouse
    total_selling_price = selling_price * 2
    result = total_selling_price
    return result

print(solution())