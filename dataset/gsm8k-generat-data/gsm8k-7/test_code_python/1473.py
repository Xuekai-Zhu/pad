def solution():
    jan_sales = 15
    feb_sales = 16
    total_sales = 47 # 16 average sales for 3 months, so 16 * 3 = 48
    mar_sales = total_sales - jan_sales - feb_sales # Subtract previous sales from total to get March sales
    result = mar_sales
    return result

print(solution())