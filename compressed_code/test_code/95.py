def solution():
    
    bulk_price = 12.00
    bulk_cans = 48
    bulk_per_can = bulk_price / bulk_cans
    grocery_price = 6.00
    grocery_cans = 12
    grocery_per_can = grocery_price / grocery_cans
    difference_per_can = (grocery_per_can - bulk_per_can) * 100
    result = difference_per_can
    return result

print(solution())