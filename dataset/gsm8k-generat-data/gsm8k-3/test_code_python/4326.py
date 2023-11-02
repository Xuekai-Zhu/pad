def solution():
    """Liam and Claire picked and sold oranges to save for their mother's birthday gift. Liam picked 40 oranges and sold them at $2.50 for 2 while Claire picked 30 oranges and sold them at $1.20 each. If all of their oranges were sold, how much are they going to save for their mother's birthday gift?"""
    # Calculate Liam's earnings from selling oranges
    liam_oranges = 40
    liam_price = 2.50
    liam_total_price = (liam_oranges // 2) * liam_price
    liam_remaining_oranges = liam_oranges % 2
    liam_remaining_price = liam_remaining_oranges * (liam_price / 2)
    liam_total_earnings = liam_total_price + liam_remaining_price

    # Calculate Claire's earnings from selling oranges
    claire_oranges = 30
    claire_price = 1.20
    claire_total_earnings = claire_oranges * claire_price

    # Calculate the total amount saved for their mother's gift
    total_earnings = liam_total_earnings + claire_total_earnings

    # Display the total amount saved
    result = total_earnings
    return result

print(solution())