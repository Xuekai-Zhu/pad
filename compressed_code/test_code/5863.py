def solution():
    
    total_sales = 36
    fabric_sales = total_sales * 1/3
    jewelry_sales = total_sales * 1/4
    stationery_sales = total_sales - fabric_sales - jewelry_sales
    result = stationery_sales
    return result

print(solution())