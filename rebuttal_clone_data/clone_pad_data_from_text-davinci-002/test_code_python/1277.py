def solution():
    total_apples = 64
    baskets = 4
    apples_stolen = 3
    apples_per_basket = (total_apples - (apples_stolen * baskets)) / baskets
    result = apples_per_basket
    return result

print(solution())