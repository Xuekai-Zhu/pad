def solution():
    
    total_sales = 72
    laptops = total_sales / 2
    netbooks = total_sales / 3
    desktops = total_sales - laptops - netbooks
    result = desktops
    return result

print(solution())