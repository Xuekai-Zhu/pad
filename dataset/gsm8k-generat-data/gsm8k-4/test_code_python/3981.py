def solution():
    """James visits 20 houses to try and make a sale. He manages to sell something in every house. The next day he visits twice as many houses but only sold to 80% of houses. If he sold two things at each house in each of the two days, how many items did he sell?"""
    # Define the number of houses visited and the sales made on each day
    houses_day1 = 20
    sales_day1 = houses_day1 * 1  # sold something in every house

    houses_day2 = 2 * houses_day1
    sales_day2 = int(houses_day2 * 0.8)  # sold to 80% of houses

    # Calculate the total number of items sold
    total_sales = 2 * (sales_day1 + sales_day2)

    # Return the result
    result = total_sales
    return result

print(solution())