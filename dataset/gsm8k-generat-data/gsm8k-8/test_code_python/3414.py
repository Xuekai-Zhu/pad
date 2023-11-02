def solution():
    baskets_per_week = 3
    crabs_per_basket = 4
    total_crabs_per_week = baskets_per_week * crabs_per_basket
    crabs_collected_twice_a_week = total_crabs_per_week * 2
    price_per_crab = 3
    total_earnings = crabs_collected_twice_a_week * price_per_crab
    result = total_earnings
    return result

print(solution())