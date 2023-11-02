def solution():
    
    weight_pair_socks = 2
    weight_underwear = 4
    weight_shirt = 5
    weight_shorts = 8
    weight_pants = 10
    total_weight_used = (weight_pants * 1) + (weight_shorts * 1) + (weight_shirt * 2) + (weight_pair_socks * 3)
    max_weight_allowed = 50
    remaining_weight_allowed = max_weight_allowed - total_weight_used
    max_pairs_of_underwear = remaining_weight_allowed // weight_underwear
    result = max_pairs_of_underwear
    return result

print(solution())