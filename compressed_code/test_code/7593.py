def solution():
    
    total_pairs = 10
    shoes_per_pair = 2
    polished_percent = 45
    polished_shoes = total_pairs * shoes_per_pair * (polished_percent / 100)
    remaining_shoes = total_pairs * shoes_per_pair - polished_shoes
    result = remaining_shoes
    return result

print(solution())