def solution():
    
    total_sales = 50
    small_sales = 11
    medium_sales = 24
    small_price = 1
    medium_price = 2
    large_price = 3
    
    
    
    
    
    large_cups_sold = (total_sales - (small_sales + medium_sales)) / large_price
    
    result = large_cups_sold
    
    return result

print(solution())