def solution():
    
    kristine_barrettes = 1
    kristine_comb = 1
    crystal_barrettes = 3
    crystal_comb = 1
    barrettes_price = 3
    comb_price = 1
    kristine_spending = kristine_barrettes * barrettes_price + kristine_comb * comb_price
    crystal_spending = crystal_barrettes * barrettes_price + crystal_comb * comb_price
    total_spending = kristine_spending + crystal_spending
    result = total_spending
    return result

print(solution())