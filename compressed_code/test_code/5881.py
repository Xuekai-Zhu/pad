def solution():
    
    bulk_can_price = 12 / 48
    grocery_can_price = 6 / 12
    difference_per_can = (grocery_can_price - bulk_can_price) * 100
    result = round(difference_per_can)
    return result

print(solution())