def solution():
    
    monday_sales = 12
    tuesday_sales = 3 * monday_sales
    wednesday_sales = tuesday_sales / 3
    total_sales = monday_sales + tuesday_sales + wednesday_sales
    result = total_sales
    return result

print(solution())