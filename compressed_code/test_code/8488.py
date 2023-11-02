def solution():
    
    baskets_per_week = 3
    crabs_per_basket = 4
    collections_per_week = 2
    price_per_crab = 3
    total_crabs = baskets_per_week * crabs_per_basket * collections_per_week
    money_made = total_crabs * price_per_crab
    result = money_made
    return result

print(solution())