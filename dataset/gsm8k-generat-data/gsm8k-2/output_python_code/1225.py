def solution():
    """Nina makes one-of-a-kind jewelry and sells it at a local boutique. She charges $25.00 for her necklaces, $15.00 for bracelets and $10.00 for a pair of earrings. Over the weekend, she sold 5 necklaces, 10 bracelets, 20 earrings, and received 2 orders for a complete jewelry ensemble that Nina charged $45.00 for. How much money did she make over the weekend?"""
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