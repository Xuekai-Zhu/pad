def solution():
    
    
    dimes = 350
    quarters = dimes / 5
    quarters_set_aside = (2/5) * quarters
    remaining_quarters = quarters - quarters_set_aside
    
    total_coins = dimes + remaining_quarters
    
    result = total_coins
    return result

print(solution())