def solution():
    
    log_length = 20
    cut_length = log_length / 2
    weight_per_foot = 150
    weight_per_cut_piece = cut_length * weight_per_foot
    result = weight_per_cut_piece
    return result

print(solution())