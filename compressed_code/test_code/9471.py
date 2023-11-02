def solution():
    
    total_shirts = 20
    total_shorts = 8
    folded_shirts = 12
    folded_shorts = 5
    remaining_shirts = total_shirts - folded_shirts
    remaining_shorts = total_shorts - folded_shorts
    remaining_pieces = remaining_shirts + remaining_shorts
    result = remaining_pieces
    return result

print(solution())