def solution():
    # Calculate the number of screens Bennett sold in February
    feb_sales = 2 * jan_sales

    # Calculate the number of screens Bennett sold in March
    mar_sales = 8800

    # Calculate the number of screens Bennett sold in January
    jan_sales = mar_sales / (2 * 4)

    # Calculate the total number of screens Bennett sold from January to March
    total_sales = jan_sales + feb_sales + mar_sales
    result = total_sales
    return result

print(solution())