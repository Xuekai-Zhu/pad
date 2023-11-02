def solution():
    """Shem makes 2.5 times more money per hour than Kem. If Kem earns $4 per hour, how much does Shem earn for an 8-hour workday?"""
    # Define Kem's hourly wage
    kem_wage = 4

    # Calculate Shem's hourly wage
    shem_wage = 2.5 * kem_wage

    # Calculate Shem's total earnings for an 8-hour workday
    shem_earnings = shem_wage * 8

    # Return the result
    result = shem_earnings
    return result

print(solution())