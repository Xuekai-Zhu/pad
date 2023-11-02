def solution():
    """Kendra and Laurel have shops that sell different brands of shoe collections. In 2014, Kendra made $8000 less than Laurel made in sales.
    However, in 2015, Kendra made 20% more money than Laurel made in 2014. If Laurel earned $30000 in 2014, calculate Kendra's total earnings in the two years."""
    # Calculate Kendra's earnings in 2014
    kendra_earnings_2014 = 30000 - 8000

    # Calculate Laurel's earnings in 2015
    laurel_earnings_2015 = 1.2 * 30000

    # Calculate Kendra's earnings in 2015
    kendra_earnings_2015 = 1.2 * laurel_earnings_2014

    # Calculate Kendra's total earnings in the two years
    total_earnings = kendra_earnings_2014 + kendra_earnings_2015

    # Display Kendra's total earnings
    result = total_earnings
    return result

print(solution())