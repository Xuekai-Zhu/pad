def solution():
    """Kendra and Laurel have shops that sell different brands of shoe collections. In 2014, Kendra made $8000 less than Laurel made in sales. However, in 2015, Kendra made 20% more money than Laurel made in 2014. If Laurel earned $30000 in 2014, calculate Kendra's total earnings in the two years."""
    laurel_sales_2014 = 30000
    kendra_sales_2014 = laurel_sales_2014 - 8000
    laurel_sales_2015 = laurel_sales_2014
    kendra_sales_2015 = laurel_sales_2014 * 1.2
    total_earnings = laurel_sales_2014 + kendra_sales_2014 + laurel_sales_2015 + kendra_sales_2015
    result = total_earnings
    return result

print(solution())