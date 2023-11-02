def solution():
    
    pineapples_bought = 6
    cost_per_pineapple = 3
    pineapple_rings_per_pineapple = 12
    pineapple_rings_sold = 4
    price_per_pineapple_ring = 5
    cost_of_pineapples = pineapples_bought * cost_per_pineapple
    total_pineapple_rings = pineapples_bought * pineapple_rings_per_pineapple
    pineapple_rings_to_sell = total_pineapple_rings // pineapple_rings_sold
    profit = (pineapple_rings_to_sell * price_per_pineapple_ring) - cost_of_pineapples
    result = profit
    return result

print(solution())