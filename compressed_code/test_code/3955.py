def solution():
    
    fries_price = 2
    salad_price = 3 * fries_price
    total_price = 15
    burger_price = (total_price - (2 * fries_price) - salad_price) / 1
    result = burger_price
    return result

print(solution())