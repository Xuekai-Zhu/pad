def solution():
    total_sales = 72
    laptop_sales = total_sales / 2
    netbook_sales = total_sales / 3
    desktop_sales = total_sales - laptop_sales - netbook_sales
    result = desktop_sales
    return result

print(solution())