def solution():
    """Shem makes 2.5 times more money per hour than Kem. If Kem earns $4 per hour, how much does Shem earn for an 8-hour workday?"""
    # Define Kem's hourly rate
    KEM_RATE = 4

    # Calculate Shem's hourly rate
    SHEM_RATE = 2.5 * KEM_RATE

    # Calculate Shem's earnings for an 8-hour workday
    SHEM_EARNINGS = 8 * SHEM_RATE

    # Display Shem's earnings
    result = SHEM_EARNINGS
    return result

print(solution())