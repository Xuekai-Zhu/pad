def solution():
    num_candies = 60
    candies_per_pack = 20

    # Calculate the number of packs Antonov gave away
    packs_given_away = 1

    # Calculate the number of packs Antonov still has
    packs_remaining = (num_candies - (packs_given_away * candies_per_pack)) / candies_per_pack
    result = packs_remaining
    return result

print(solution())