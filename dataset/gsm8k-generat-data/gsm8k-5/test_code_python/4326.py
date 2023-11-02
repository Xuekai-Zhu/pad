def solution():
    # Calculate Liam's earnings
    liam_oranges = 40
    liam_price = 2.5
    liam_sold = 2
    liam_earnings = liam_oranges * liam_price * liam_sold

    # Calculate Claire's earnings
    claire_oranges = 30
    claire_price = 1.2
    claire_earnings = claire_oranges * claire_price

    # Calculate total earnings
    total_earnings = liam_earnings + claire_earnings
    result = total_earnings
    return result

print(solution())