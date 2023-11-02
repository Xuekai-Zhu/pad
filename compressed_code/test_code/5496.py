def solution():
    
    single_balloon_price = 0.5
    pack_price = 3
    pack_size = 10
    total_price = 0
    full_packs = 14 // pack_size
    rest_balloons = 14 % pack_size
    total_price += full_packs * pack_price
    total_price += rest_balloons * single_balloon_price
    result = total_price
    return result

print(solution())