def solution():
    white_shirts = 2
    blue_shirts = 4
    white_shirt_packs = 5
    blue_shirt_packs = 3
    white_shirt_cost = 3
    blue_shirt_cost = 3
    total_white_shirts = white_shirts * white_shirt_packs
    total_blue_shirts = blue_shirts * blue_shirt_packs
    total_shirts = total_white_shirts + total_blue_shirts
    total_cost = total_shirts * shirt_cost
    result = total_cost
    return result

print(solution())