def solution():
    
    necklace_price = 25
    bracelet_price = 15
    earrings_price = 10
    ensemble_price = 45
    
    necklaces_sold = 5
    bracelets_sold = 10
    earrings_sold = 20
    ensembles_sold = 2
    
    total_money = (necklaces_sold * necklace_price) + (bracelets_sold * bracelet_price) + (earrings_sold * earrings_price) + (ensembles_sold * ensemble_price)
    
    result = total_money
    return result

print(solution())