def solution():
    # Calculate Kendra's sales in 2014
    laurel_sales_2014 = 30000
    kendra_sales_2014 = laurel_sales_2014 - 8000

    # Calculate Laurel's sales in 2015
    laurel_sales_2015 = laurel_sales_2014 * 1.2

    # Calculate Kendra's sales in 2015
    kendra_sales_2015 = laurel_sales_2014 * 1.2 + 8000

    # Calculate Kendra's total earnings in both years
    kendra_total_earnings = kendra_sales_2014 + kendra_sales_2015
    result = kendra_total_earnings
    return result

print(solution())