def solution():
    num_lemons = 80
    lemon_price_original = 8
    lemon_price_new = lemon_price_original + 4

    num_grapes = 140
    grape_price_original = 7
    grape_price_new = grape_price_original + (4 / 2)

    # Calculate the total earnings from selling lemons at the new price
    lemon_earnings_new = num_lemons * lemon_price_new

    # Calculate the total earnings from selling grapes at the new price
    grape_earnings_new = num_grapes * grape_price_new

    # Calculate the total earnings from selling all fruits at the new prices
    total_earnings_new = lemon_earnings_new + grape_earnings_new
    result = total_earnings_new
    return result

print(solution())