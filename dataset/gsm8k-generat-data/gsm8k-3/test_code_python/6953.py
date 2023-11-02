def solution():
    """Haleigh decides that instead of throwing away old candles, she can use the last bit of wax combined together to make new candles. Each candle has 10% of it's original wax left. How many 5 ounce candles can she make if she has five 20 oz candles, 5 five ounce candles, and twenty-five one ounce candles?"""
    # Define the amount of wax in each candle
    TWENTY_OZ_WAX = 20 * 16 * 0.1  # 20 ounces * 16 ounces/pound * 10% = 3.2 ounces
    FIVE_OZ_WAX = 5 * 0.1  # 5 ounces * 10% = 0.5 ounces
    ONE_OZ_WAX = 1 * 0.1  # 1 ounce * 10% = 0.1 ounces

    # Calculate the total amount of wax Haleigh has
    total_wax = (5 * TWENTY_OZ_WAX) + (5 * FIVE_OZ_WAX) + (25 * ONE_OZ_WAX)

    # Calculate the number of 5 ounce candles Haleigh can make
    num_candles = total_wax // 0.5

    # Display the number of candles Haleigh can make
    result = num_candles
    return result

print(solution())