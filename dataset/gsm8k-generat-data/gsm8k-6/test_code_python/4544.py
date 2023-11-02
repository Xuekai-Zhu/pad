def solution():
    # Calculate Kendra's earnings in 2014
    laurel_sales_2014 = 30000
    kendra_sales_2014 = laurel_sales_2014 - 8000

    # Calculate Kendra's earnings in 2015
    laurel_sales_2015 = laurel_sales_2014  # assume Laurel's sales remained the same in 2015
    kendra_sales_2015 = 1.2 * laurel_sales_2014  # Kendra made 20% more money than Laurel made in 2014

    # Calculate Kendra's total earnings in the two years
    kendra_total_earnings = kendra_sales_2014 + kendra_sales_2015
    result = kendra_total_earnings
    return result

print(solution())