def solution():
    
    fudge_weight = 20
    fudge_price_per_pound = 2.5
    truffles_price = 1.5
    truffles_quantity = 5 * 12
    pretzels_price = 2
    pretzels_quantity = 3 * 12
    total_sales = (fudge_weight * fudge_price_per_pound) + (truffles_quantity * truffles_price) + (pretzels_quantity * pretzels_price)
    result = total_sales
    return result

print(solution())