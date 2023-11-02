def solution():
    """Gloria has five times as many dimes as quarters in her graduation money. 
    She decides to put 2/5 of the quarters aside for future use. If she has 350 dimes, 
    calculate the combined number of quarters and dimes she has after putting aside 2/5 of the quarters?"""
    
    dimes = 350
    quarters = dimes / 5
    quarters_set_aside = (2/5) * quarters
    remaining_quarters = quarters - quarters_set_aside
    
    total_coins = dimes + remaining_quarters
    
    result = total_coins
    return result

print(solution())