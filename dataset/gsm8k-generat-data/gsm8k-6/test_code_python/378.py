def solution():
    # Calculate the total earnings of Uki for 1 day
    cupcakes = 20
    cookies = 10
    biscuits = 20
    total_earnings = (cupcakes * 1.5) + (cookies * 2) + (biscuits * 1)

    # Calculate the total earnings of Uki for 5 days
    total_earnings_5_days = total_earnings * 5
    result = total_earnings_5_days
    return result

print(solution())