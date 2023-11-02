def solution():
    # Define the fraction of sales in each section
    fabric_sales_fraction = 1/3
    jewelry_sales_fraction = 1/4

    # Calculate the fraction of sales in the stationery section
    stationery_sales_fraction = 1 - fabric_sales_fraction - jewelry_sales_fraction

    # Calculate the number of sales in the stationery section
    total_sales = 36
    stationery_sales = stationery_sales_fraction * total_sales
    result = stationery_sales
    return result

print(solution())