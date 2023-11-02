def solution():
    initial_sales = 327
    sales_increase = 50
    num_years = 3

    # Calculate the sales in the next three years
    sales = initial_sales
    for i in range(num_years):
        sales += sales_increase

    result = sales
    return result

print(solution())