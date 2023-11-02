def solution():
    
    tuesday_sales = 7
    wednesday_sales = 3 * tuesday_sales
    thursday_sales = 3 * wednesday_sales
    total_sales = tuesday_sales + wednesday_sales + thursday_sales
    result = total_sales
    return result

print(solution())