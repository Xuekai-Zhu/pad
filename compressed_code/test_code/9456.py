def solution():
    
    total_sales = 80
    wireless_sales = total_sales / 2
    optical_sales = total_sales / 4
    trackball_sales = total_sales - wireless_sales - optical_sales
    result = trackball_sales
    return result

print(solution())