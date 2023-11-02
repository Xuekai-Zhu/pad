def solution():
    
    bottles_per_pack = 6
    packs = 3
    total_bottles = bottles_per_pack * packs
    bottles_per_day = 0.5
    bottles_consumed = bottles_per_day * 7 * 4
    bottles_left = total_bottles - bottles_consumed
    result = bottles_left
    return result

print(solution())