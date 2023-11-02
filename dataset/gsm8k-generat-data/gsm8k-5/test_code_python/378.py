def solution():
    # Calculate Uki's earnings for one day
    cupcakes_earnings = 20 * 1.5  # Uki earns $1.50 from each cupcake
    cookies_earnings = 10 * 2  # Uki earns $2 from each packet of cookies
    biscuits_earnings = 20 * 1  # Uki earns $1 from each packet of biscuits
    daily_earnings = cupcakes_earnings + cookies_earnings + biscuits_earnings

    # Calculate Uki's total earnings for five days
    total_earnings = daily_earnings * 5
    result = total_earnings
    return result

print(solution())