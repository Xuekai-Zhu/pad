def solution():
    monday_sales = 40
    tuesday_sales = monday_sales + 40
    wednesday_sales = tuesday_sales / 2
    thursday_sales = wednesday_sales + 3

    total_sales = monday_sales + tuesday_sales + wednesday_sales + thursday_sales
    result = total_sales
    return result

print(solution())