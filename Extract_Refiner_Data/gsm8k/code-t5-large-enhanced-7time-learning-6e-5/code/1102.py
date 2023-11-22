def solution():
    
    total_length = 100
    parts_per_cut = 4
    parts_total = parts_per_cut * (total_length / parts_per_cut)
    cut_length = parts_total / parts_total
    result = cut_length
    return result

print(solution())