def solution():
    # Calculate Liam's earnings
    liam_oranges = 40
    liam_orange_price = 2.5 / 2
    liam_earnings = liam_oranges * liam_orange_price

    # Calculate Claire's earnings
    claire_oranges = 30
    claire_orange_price = 1.2
    claire_earnings = claire_oranges * claire_orange_price

    # Calculate the total earnings
    total_earnings = liam_earnings + claire_earnings
    result = total_earnings
    return result

print(solution())