def solution():
    Friday_sales = 40
    Saturday_sales = (2 * Friday_sales) - 10
    Sunday_sales = Saturday_sales / 2
    total_sales = Friday_sales + Saturday_sales + Sunday_sales
    result = total_sales
    return result

print(solution())