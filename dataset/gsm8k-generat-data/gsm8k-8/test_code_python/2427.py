def solution():
    # Define the amount of beef sold each day
    thurs_sales = 210
    fri_sales = 2 * thurs_sales
    sat_sales = 150

    # Calculate the total amount of beef sold
    total_sales = thurs_sales + fri_sales + sat_sales

    # Calculate the average amount of beef sold per day
    avg_sales_per_day = total_sales / 3
    result = avg_sales_per_day
    return result

print(solution())