def solution():
    
    monday_sales = 5
    tuesday_sales = monday_sales * 2
    wednesday_sales = tuesday_sales - 2
    thursday_sales = tuesday_sales / 2
    total_sales = monday_sales + tuesday_sales + wednesday_sales + thursday_sales
    result = total_sales
    return result

print(solution())