def solution():
    
    black_shirt_packs = 3
    yellow_shirt_packs = 3
    black_shirts_per_pack = 5
    yellow_shirts_per_pack = 2
    total_black_shirts = black_shirt_packs * black_shirts_per_pack
    total_yellow_shirts = yellow_shirt_packs * yellow_shirts_per_pack
    total_shirts = total_black_shirts + total_yellow_shirts
    result = total_shirts
    return result

print(solution())