def solution():
    Friday_sales = 30
    Saturday_sales = Friday_sales * 2
    Sunday_sales = Saturday_sales - 15
    total_sales = Friday_sales + Saturday_sales + Sunday_sales
    
    return total_sales

print(solution())