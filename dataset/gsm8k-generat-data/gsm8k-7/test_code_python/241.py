def solution():
    total_sales = 72

    # Calculate the number of laptops sold
    laptops_sold = total_sales / 2

    # Calculate the number of netbooks sold
    netbooks_sold = total_sales / 3

    # Calculate the number of desktop computers sold
    desktops_sold = total_sales - laptops_sold - netbooks_sold
    result = desktops_sold
    return result

print(solution())