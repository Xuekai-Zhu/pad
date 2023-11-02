def solution():
    
    trees = 10
    oranges_per_day = 12
    oranges_per_week = trees * oranges_per_day * 7
    oranges_per_pack = 6
    packs_per_week = oranges_per_week // oranges_per_pack
    price_per_pack = 2
    total_earnings = packs_per_week * price_per_pack * 3
    result = total_earnings
    return result

print(solution())