def solution():
    # Calculate Liam's earnings
    liam_orange_pairs = 40 // 2  # Liam sold his oranges in pairs
    liam_earnings = liam_orange_pairs * 2.5

    # Calculate Claire's earnings
    claire_earnings = 30 * 1.2

    # Calculate the total earnings
    total_earnings = liam_earnings + claire_earnings
    result = total_earnings
    return result

print(solution())