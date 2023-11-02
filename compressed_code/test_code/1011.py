def solution():
    
    oyster_price = 15
    shrimp_price = 14
    clams_price = 13.5
    num_oysters = 3 * 12
    num_shrimp = 2
    num_clams = 2
    total_price = (oyster_price * 3 + shrimp_price * num_shrimp + clams_price * num_clams) / 4
    result = total_price
    return result

print(solution())