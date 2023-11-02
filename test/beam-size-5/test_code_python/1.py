def solution():
    
    glass1_price = 5
    glass2_price = 0.6 * glass1_price
    num_glasses = 16
    total_price = (num_glasses * glass1_price) + (num_glasses * glass2_price)
    result = total_price
    return result

print(solution())