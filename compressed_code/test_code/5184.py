def solution():
    
    charms_per_necklace = 10
    charm_cost = 15
    necklace_price = 200
    necklaces_sold = 30
    total_charm_cost = charms_per_necklace * necklaces_sold * charm_cost
    total_necklace_earnings = necklaces_sold * necklace_price
    total_profit = total_necklace_earnings - total_charm_cost
    result = total_profit
    return result

print(solution())