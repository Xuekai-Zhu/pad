def solution():
    
    fudge_weight = 20
    fudge_price_per_pound = 2.5
    truffle_quantity = 5 * 12
    truffle_price = 1.5
    pretzel_quantity = 3 * 12
    pretzel_price = 2.0
    
    fudge_sales = fudge_weight * fudge_price_per_pound
    truffle_sales = truffle_quantity * truffle_price
    pretzel_sales = pretzel_quantity * pretzel_price
    
    total_sales = fudge_sales + truffle_sales + pretzel_sales
    result = total_sales
    
    return result

print(solution())