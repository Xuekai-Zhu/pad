def solution():
    
    sofa_price = 1250
    armchair_price = 425
    total_price = 2430
    armchair_total_price = 2 * armchair_price
    coffee_table_price = total_price - sofa_price - armchair_total_price
    result = coffee_table_price
    return result

print(solution())