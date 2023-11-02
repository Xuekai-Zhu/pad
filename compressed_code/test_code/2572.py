def solution():
    
    pieces_per_birdhouse = 7
    cost_per_piece = 1.5
    profit_per_birdhouse = 5.5
    cost_per_birdhouse = pieces_per_birdhouse * cost_per_piece
    price_per_birdhouse = cost_per_birdhouse + profit_per_birdhouse
    total_price = price_per_birdhouse * 2
    result = total_price
    return result

print(solution())