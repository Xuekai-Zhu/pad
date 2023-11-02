def solution():
    # Calculate Tobias's earnings from selling red tractors
    red_tractor_earnings = 2 * 0.1 * 20000  # Tobias gets paid 10% of the sales price for each red tractor sold

    # Calculate Tobias's earnings from selling green tractors
    green_tractor_earnings = 3 * 0.2 * x  # Tobias gets paid 20% of the sales price for each green tractor sold

    # Calculate the full price of a single green tractor
    total_earnings = red_tractor_earnings + green_tractor_earnings  # Tobias's total earnings
    x = (7000 - red_tractor_earnings) / (3 * 0.2)  # solve for the price of a single green tractor

    result = x
    return result

print(solution())