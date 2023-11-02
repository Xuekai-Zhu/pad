def solution():
    """On the first day of the garden center sale, 14 marigolds were sold. The next day 25 more marigolds were sold. On the third day the center sold two times the number of marigolds it did on the day before. How many marigolds were sold during the sale?"""
    # Define the initial number of marigolds sold and the increase in sales each day
    day1_sales = 14
    day2_sales_increase = 25
    day3_sales_increase = 2

    # Calculate the number of marigolds sold on the second day
    day2_sales = day1_sales + day2_sales_increase

    # Calculate the number of marigolds sold on the third day
    day3_sales = day2_sales * day3_sales_increase

    # Calculate the total number of marigolds sold
    total_sales = day1_sales + day2_sales + day3_sales

    # Return the result
    result = total_sales
    return result

print(solution())