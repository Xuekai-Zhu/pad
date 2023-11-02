def solution():
    """Kendra and Laurel have shops that sell different brands of shoe collections. In 2014, Kendra made $8000 less than Laurel made in sales. However, in 2015, Kendra made 20% more money than Laurel made in 2014. If Laurel earned $30000 in 2014, calculate Kendra's total earnings in the two years."""
    # Laurel's sales in 2014
    laurel_sales_2014 = 30000

    # Kendra's sales in 2014
    kendra_sales_2014 = laurel_sales_2014 - 8000

    # Laurel's sales in 2015 (20% more than her 2014 sales)
    laurel_sales_2015 = laurel_sales_2014 * 1.2

    # Kendra's sales in 2015 (20% more than Laurel's 2014 sales)
    kendra_sales_2015 = kendra_sales_2014 * 1.2

    # Calculate Kendra's total earnings
    kendra_total_earnings = kendra_sales_2014 + kendra_sales_2015

    # Calculate Laurel's total earnings
    laurel_total_earnings = laurel_sales_2014 + laurel_sales_2015

    # Calculate the sum of Kendra's and Laurel's total earnings
    total_earnings = kendra_total_earnings + laurel_total_earnings

    # return the result
    result = total_earnings
    return result

print(solution())