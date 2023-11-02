def solution():
    
    total_weight = 0
    pants_weight = 10
    shirts_weight = 2 * 5
    shorts_weight = 8
    socks_weight = 3 * 2
    total_weight = pants_weight + shirts_weight + shorts_weight + socks_weight
    max_weight = 50
    remaining_weight = max_weight - total_weight
    underwear_weight = 4
    max_undies = remaining_weight // underwear_weight
    result = max_undies
    return result

print(solution())