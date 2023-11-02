def solution():
    kem_earnings_per_hour = 4  # Kem earns $4 per hour
    shem_earnings_per_hour = 2.5 * kem_earnings_per_hour  # Shem earns 2.5 times more than Kem
    shem_workday_earnings = shem_earnings_per_hour * 8  # Shem works an 8-hour day

    result = shem_workday_earnings
    return result

print(solution())