def solution():
    
    candy_per_house_anna = 14
    candy_per_house_billy = 11
    houses_anna = 60
    houses_billy = 75
    candy_anna = candy_per_house_anna * houses_anna
    candy_billy = candy_per_house_billy * houses_billy
    difference = candy_anna - candy_billy
    result = difference
    return result

print(solution())