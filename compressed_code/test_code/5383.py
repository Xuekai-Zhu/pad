def solution():
    
    total_earnings = 85
    j_ratio = 4
    l_earnings = total_earnings / (j_ratio + 1)
    j_earnings = j_ratio * l_earnings
    result = j_earnings
    return result

print(solution())