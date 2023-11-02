def solution():
    baskets_per_week = 3
    crabs_per_basket = 4
    crabs_per_week = baskets_per_week * crabs_per_basket
    crabs_per_collection = crabs_per_week / 2
    price_per_crab = 3
    total_income = crabs_per_collection * price_per_crab
    result = total_income
    return result

print(solution())