def solution():
    necklaces_sold = 5
    bracelets_sold = 10
    earrings_sold = 20
    ensemble_sold = 2
    necklace_price = 25
    bracelet_price = 15
    earring_price = 10
    ensemble_price = 45
    total_sales = (necklaces_sold * necklace_price) + (bracelets_sold * bracelet_price) + (earrings_sold * earring_price) + (ensemble_sold * ensemble_price)
    result = total_sales
    return result

print(solution())