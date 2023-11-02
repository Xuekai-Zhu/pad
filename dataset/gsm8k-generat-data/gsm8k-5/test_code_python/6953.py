def solution():
    # Calculate the total amount of wax available from the old candles
    total_wax = (5 * 20 * 0.1) + (5 * 5 * 0.1) + (25 * 1 * 0.1) # 5 20 oz candles, 5 5 oz candles, and 25 1 oz candles, each with 10% of its original wax left

    # Calculate the total number of 5 ounce candles that can be made
    num_candles = total_wax / 0.5 # Each new 5 oz candle requires 0.5 oz of wax

    result = num_candles
    return result

print(solution())