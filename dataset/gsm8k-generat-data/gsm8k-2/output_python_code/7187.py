def solution():
    """Shem makes 2.5 times more money per hour than Kem. If Kem earns $4 per hour, how much does Shem earn for an 8-hour workday?"""
    kem_hourly_rate = 4
    shem_hourly_rate = 2.5 * kem_hourly_rate
    shem_daily_earnings = shem_hourly_rate * 8
    result = shem_daily_earnings
    return result

print(solution())