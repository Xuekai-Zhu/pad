def solution():
    kem_earnings_per_hour = 4
    shem_earnings_per_hour = 2.5 * kem_earnings_per_hour
    hours_worked = 8

    # Calculate Shem's total earnings for the day
    shem_total_earnings = shem_earnings_per_hour * hours_worked

    result = shem_total_earnings
    return result

print(solution())