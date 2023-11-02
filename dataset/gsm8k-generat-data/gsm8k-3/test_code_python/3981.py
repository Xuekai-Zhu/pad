def solution():
    """James visits 20 houses to try and make a sale.  He manages to sell something in every house.  The next day he visits twice as many houses but only sold to 80% of houses.  If he sold two things at each house in each of the two days, how many items did he sell?"""
    # Define the number of houses visited and the sales rate for the first day
    houses1 = 20
    sales_rate1 = 1

    # Define the number of houses visited and the sales rate for the second day
    houses2 = 2 * houses1
    sales_rate2 = 0.8

    # Calculate the total number of sales for the first day
    sales1 = houses1 * sales_rate1 * 2

    # Calculate the total number of sales for the second day
    sales2 = houses2 * sales_rate2 * 2

    # Calculate the total number of sales over both days
    total_sales = sales1 + sales2

    # Display the total number of sales
    result = total_sales
    return result

print(solution())