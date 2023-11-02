def solution():
    milk_per_day = 16
    kids_consumption = 0.75  # 75% of the milk is consumed by Daisy's kids
    remaining_milk1 = milk_per_day * (1 - kids_consumption)  # remaining milk after kids consume their share
    cooking_share = 0.5  # 50% of the remaining milk is used for cooking
    remaining_milk2 = remaining_milk1 * (1 - cooking_share)  # remaining milk after cooking
    result = remaining_milk2
    return result

print(solution())