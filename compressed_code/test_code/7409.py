def solution():
    
    wednesday_sales = 15
    thursday_sales = 3 * wednesday_sales
    friday_sales = thursday_sales // 5
    total_sales = wednesday_sales + thursday_sales + friday_sales
    result = total_sales
    return result

print(solution())