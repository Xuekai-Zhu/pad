def solution():
    candies_bought = 300
    percent_sour = 40
    candies_sour = candies_bought * (percent_sour / 100)
    candies_good = candies_bought - candies_sour
    candies_per_person = candies_good / 3
    result = candies_per_person
    return result

print(solution())