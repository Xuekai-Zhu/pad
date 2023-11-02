def solution():
    """Helen cuts her lawn starting in March and finishes in October.  Her lawn mower uses 2 gallons of gas every 4th time she cuts her lawn.  For March, April, September and October, she only cuts her law 2 times per month.  In May, June, July and August, she has to cut her lawn 4 times per month.  How many gallons of gas will she need to cut her lawn from March through October?"""
    # Define the number of times Helen cuts her lawn each month
    MARCH_TO_AUG_CUTS = 4
    OTHER_MONTH_CUTS = 2

    # Define the frequency of gas usage
    GAS_USE_FREQUENCY = 4
    GAS_PER_USE = 2

    # Define the number of months Helen cuts her lawn
    months_cutting = 8

    # Calculate the total number of times Helen cuts her lawn
    march_to_august = MARCH_TO_AUG_CUTS * 4
    other_months = OTHER_MONTH_CUTS * 4
    total_cuts = march_to_august + other_months

    # Calculate the number of times Helen uses gas
    gas_uses = total_cuts // GAS_USE_FREQUENCY
    if total_cuts % GAS_USE_FREQUENCY != 0:
        gas_uses += 1

    # Calculate the total amount of gas needed
    total_gas = gas_uses * GAS_PER_USE

    # Display the total amount of gas needed
    result = total_gas
    return result

print(solution())