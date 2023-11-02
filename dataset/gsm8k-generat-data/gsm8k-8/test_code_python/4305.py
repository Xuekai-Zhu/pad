def solution():
    # Define the number of crates sold each day
    monday_sales = 5
    tuesday_sales = 2 * monday_sales
    wednesday_sales = tuesday_sales - 2
    thursday_sales = tuesday_sales / 2

    # Calculate the total number of crates sold
    total_sales = monday_sales + tuesday_sales + wednesday_sales + thursday_sales
    result = total_sales
    return result

print(solution())