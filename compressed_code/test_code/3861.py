def solution():
    
    bottles_per_pack = 6
    packs = 3
    daily_consumption = 0.5
    total_bottles = bottles_per_pack * packs
    remaining_bottles = total_bottles - (daily_consumption * 7 * 4)
    result = remaining_bottles
    return result

print(solution())