def solution():
    
    total_candies = 60
    candies_per_pack = 20
    candies_given_away = candies_per_pack
    candies_remaining = total_candies - candies_given_away
    packs_remaining = candies_remaining // candies_per_pack
    result = packs_remaining
    return result

print(solution())