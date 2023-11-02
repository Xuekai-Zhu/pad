def solution():
    
    dimes = 350
    quarters = dimes // 5
    reserved_quarters = 2/5 * quarters
    remaining_quarters = quarters - reserved_quarters
    total_coins = dimes + remaining_quarters
    result = total_coins
    return result

print(solution())