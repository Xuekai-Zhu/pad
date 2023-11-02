def solution():
    
    paper_weight = 1/5
    num_paper_sheets = 8
    envelope_weight = 2/5
    total_weight = (paper_weight * num_paper_sheets) + envelope_weight
    num_stamps = total_weight
    result = num_stamps
    return result

print(solution())