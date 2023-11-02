def solution():
    thursday_sales = 210
    friday_sales = thursday_sales * 2
    saturday_sales = 150

    # Calculate the total sales over the three days
    total_sales = thursday_sales + friday_sales + saturday_sales

    # Calculate the average sales per day
    average_sales_per_day = total_sales / 3
    result = average_sales_per_day
    return result

print(solution())