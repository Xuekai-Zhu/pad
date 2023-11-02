def solution():
    total_candies = 60
    candies_per_pack = 20
    packs_given_away = 1

    packs_left = (total_candies - (candies_per_pack * packs_given_away)) / candies_per_pack
    result = packs_left
    return result

print(solution())