def solution():
    
    num_baskets = 5
    petunias_per_basket = 3
    sweet_potato_vines_per_basket = 2
    petunia_cost = 3
    sweet_potato_vine_cost = 2.5
    total_cost = (petunias_per_basket * petunia_cost) + (sweet_potato_vines_per_basket * sweet_potato_vine_cost)
    total_cost += num_baskets * total_cost
    result = total_cost
    return result

print(solution())