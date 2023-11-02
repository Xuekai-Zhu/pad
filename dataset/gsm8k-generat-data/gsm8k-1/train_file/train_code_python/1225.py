def solution():
    """Nina makes one-of-a-kind jewelry and sells it at a local boutique. She charges $25.00 for her necklaces, $15.00 for bracelets and $10.00 for a pair of earrings. Over the weekend, she sold 5 necklaces, 10 bracelets, 20 earrings, and received 2 orders for a complete jewelry ensemble that Nina charged $45.00 for. How much money did she make over the weekend?"""
    necklace_price = 25
    bracelet_price = 15
    earrings_price = 10
    jewelry_ensemble_price = 45

    total_necklace_sales = 5 * necklace_price
    total_bracelet_sales = 10 * bracelet_price
    total_earrings_sales = 20 * earrings_price
    total_jewelry_ensemble_sales = 2 * jewelry_ensemble_price

    total_sales = (
        total_necklace_sales
        + total_bracelet_sales
        + total_earrings_sales
        + total_jewelry_ensemble_sales
    )

    result = total_sales
    return result

print(solution())