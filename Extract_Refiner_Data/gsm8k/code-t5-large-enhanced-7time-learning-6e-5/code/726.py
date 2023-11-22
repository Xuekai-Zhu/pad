def solution():
    
    pieces_per_day = 4
    pieces_per_pack = 15
    days = 30
    total_pieces = pieces_per_day * days
    packs_needed = total_pieces / pieces_per_pack
    result = packs_needed
    return result

print(solution())