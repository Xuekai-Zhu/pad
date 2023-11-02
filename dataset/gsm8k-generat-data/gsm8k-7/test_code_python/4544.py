def solution():
    laural_earnings_2014 = 30000

    # Calculate Kendra's earnings in 2014
    kendra_earnings_2014 = laural_earnings_2014 - 8000

    # Calculate Laurel's earnings in 2015
    laural_earnings_2015 = laural_earnings_2014 * 1.20

    # Calculate Kendra's earnings in 2015
    kendra_earnings_2015 = laural_earnings_2015 + 8000

    # Calculate Kendra's total earnings in both years
    total_earnings = kendra_earnings_2014 + kendra_earnings_2015
    result = total_earnings
    return result

print(solution())