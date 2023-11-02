def solution():
    
    trees = 10
    oranges_per_day = 12
    days_per_week = 7
    weeks = 3
    total_oranges = trees * oranges_per_day * days_per_week * weeks
    packs_of_oranges = total_oranges // 6
    price_per_pack = 2
    total_earnings = packs_of_oranges * price_per_pack
    result = total_earnings
    return result

print(solution())