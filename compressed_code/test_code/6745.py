def solution():
    
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