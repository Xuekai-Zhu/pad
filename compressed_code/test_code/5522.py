def solution():
    
    total_macaroons = 12
    macaroon_weight = 5
    macaroons_per_bag = total_macaroons // 4
    remaining_macaroons = total_macaroons - macaroons_per_bag
    remaining_weight = remaining_macaroons * macaroon_weight
    result = remaining_weight
    return result

print(solution())