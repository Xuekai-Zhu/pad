def solution():
    
    eggplant_price = 3
    total_eggplant_sales = 20 * eggplant_price
    total_corn_sales = 135 - total_eggplant_sales
    corn_price = corn_sales / 25
    result = corn_price
    return result

print(solution())