def solution():
    bea_price = 25
    dawn_price = 28
    bea_glasses = 10
    dawn_glasses = 8

    # Calculate the total earnings for Bea
    bea_earnings = bea_price * bea_glasses

    # Calculate the total earnings for Dawn
    dawn_earnings = dawn_price * dawn_glasses

    # Calculate the difference in their earnings
    earnings_diff = bea_earnings - dawn_earnings
    result = earnings_diff
    return result

print(solution())