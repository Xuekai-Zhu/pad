def solution():
    # Day 1 sales
    day1_sales = 45

    # Day 2 sales
    day2_sales = day1_sales + 20

    # Day 3 sales
    day3_sales = (2 * day2_sales) - 10

    # Total sales for first three days
    total_sales_days1to3 = day1_sales + day2_sales + day3_sales

    # Total sales for 4 days
    total_sales_4days = 350

    # Determine sales for day 4
    day4_sales = total_sales_4days - total_sales_days1to3

    result = day4_sales
    return result

print(solution())