def solution():
    """Nina makes one-of-a-kind jewelry and sells it at a local boutique.  She charges $25.00 for her necklaces,
    $15.00 for bracelets and $10.00 for a pair of earrings.  Over the weekend, she sold 5 necklaces, 10 bracelets,
    20 earrings, and received 2 orders for a complete jewelry ensemble that Nina charged $45.00 for.
    How much money did she make over the weekend?"""
    
    # Find the total sales from necklaces
    necklace_sales = 5 * 25
    
    # Find the total sales from bracelets
    bracelet_sales = 10 * 15
    
    # Find the total sales from earrings
    earring_sales = 20 * 10
    
    # Find the total revenue from the jewelry ensembles
    ensemble_sales = 2 * 45
    
    # Calculate the total revenue earned over the weekend
    total_revenue = necklace_sales + bracelet_sales + earring_sales + ensemble_sales
    
    result = total_revenue
    return result

print(solution())