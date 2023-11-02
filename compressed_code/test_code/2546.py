def solution():
    
    seed_cost = 0.5
    seed_per_bag = 100
    corn_price = 0.1
    profit = 40
    seeds_per_corn = 4
    seeds_needed = seeds_per_corn * seed_per_bag
    cost_per_seed = seed_cost / seed_per_bag
    revenue_per_corn = corn_price
    profit_per_corn = revenue_per_corn - cost_per_seed * seeds_per_corn
    corns_sold = profit / profit_per_corn
    result = corns_sold
    return result

print(solution())