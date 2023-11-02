def solution():
    friday_sales = 181  # Addison sold 181 raffle tickets on Friday
    saturday_sales = 2 * friday_sales  # Addison sold twice as many tickets on Saturday
    sunday_sales = 78  # Addison sold 78 raffle tickets on Sunday

    # Calculate the difference in sales between Saturday and Sunday
    sales_difference = saturday_sales - sunday_sales
    result = sales_difference
    return result

print(solution())