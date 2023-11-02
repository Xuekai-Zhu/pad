def solution():
    
    burger_count = 30
    burger_price = 2
    fries_count = 12
    fries_price = 1.5
    total_burger_sales = burger_count * burger_price
    total_fries_sales = fries_count * fries_price
    total_sales = total_burger_sales + total_fries_sales
    result = total_sales
    return result

print(solution())