def solution():
    """Haleigh decides that instead of throwing away old candles, she can use the last bit of wax combined together to make new candles. Each candle has 10% of it's original wax left. How many 5 ounce candles can she make if she has five 20 oz candles, 5 five ounce candles, and twenty-five one ounce candles?"""
    # Define the amount of wax in each size of candle
    large_candle_wax = 20 * 0.1
    medium_candle_wax = 5 * 0.1
    small_candle_wax = 1 * 0.1

    # Calculate the total amount of wax available
    total_wax = (large_candle_wax * 5) + (medium_candle_wax * 5) + (small_candle_wax * 25)

    # Calculate the number of 5 oz candles that can be made
    num_candles = total_wax / 0.5
    
    # Round down to the nearest whole number
    num_candles = int(num_candles)

    # Return the result
    result = num_candles
    return result

print(solution())