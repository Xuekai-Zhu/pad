def solution():
    # Calculate the number of sales in fabric and jewelry sections
    fabric_sales = (1/3)*36
    jewelry_sales = (1/4)*36

    # Calculate the number of sales in stationery section
    stationery_sales = 36 - fabric_sales - jewelry_sales
    result = stationery_sales
    return result

print(solution())