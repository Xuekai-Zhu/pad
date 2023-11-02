def solution():
    laurel_earnings_2014 = 30000  # Laurel earned $30000 in 2014
    kendra_earnings_2014 = laurel_earnings_2014 - 8000  # Kendra made $8000 less than Laurel in 2014
    kendra_earnings_2015 = laurel_earnings_2014 * 1.2  # Kendra made 20% more money than Laurel made in 2014

    # Calculate Kendra's total earnings in the two years
    total_earnings = kendra_earnings_2014 + kendra_earnings_2015
    result = total_earnings
    return result

print(solution())