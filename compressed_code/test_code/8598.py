def solution():
    
    total_fish = 90
    swordfish_ratio = 5
    pufferfish_ratio = 1
    fish_ratio_sum = swordfish_ratio + pufferfish_ratio
    pufferfish_count = (pufferfish_ratio/fish_ratio_sum) * total_fish
    result = pufferfish_count
    return result

print(solution())