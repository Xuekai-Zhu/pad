def solution():
    candies_bought = 60  # Antonov bought 60 candies
    candies_given_away = 20  # Antonov gave away one pack of candy, which is 20 candies
    candies_remaining = candies_bought - candies_given_away  # Antonov has 40 candies remaining

    # Calculate the number of packs of candies Antonov still has
    packs_remaining = candies_remaining // 20
    result = packs_remaining
    return result

print(solution())