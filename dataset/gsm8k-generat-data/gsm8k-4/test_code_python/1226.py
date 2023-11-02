def solution():
    """Nina makes one-of-a-kind jewelry and sells it at a local boutique. She charges $25.00 for her necklaces, $15.00 for bracelets and $10.00 for a pair of earrings. Over the weekend, she sold 5 necklaces, 10 bracelets, 20 earrings, and received 2 orders for a complete jewelry ensemble that Nina charged $45.00 for. How much money did she make over the weekend?"""
    # Define the prices of necklaces, bracelets, earrings, and the complete ensemble
    necklace_price = 25
    bracelet_price = 15
    earring_price = 10
    ensemble_price = 45

    # Calculate the total sales from selling necklaces, bracelets, and earrings
    total_sales = (5 * necklace_price) + (10 * bracelet_price) + (20 * earring_price)

    # Calculate the total sales from selling the complete ensemble
    total_sales += (2 * ensemble_price)

    # Return the total sales
    result = total_sales
    return result

print(solution())