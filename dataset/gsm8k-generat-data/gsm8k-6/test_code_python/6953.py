def solution():
    # Calculate the total amount of wax Haleigh has available
    total_wax = (5 * 20 * 0.1) + (5 * 5 * 0.1) + (25 * 1 * 0.1)  # each candle has 10% of its original wax left

    # Calculate the number of 5 ounce candles Haleigh can make
    num_candles = total_wax / 0.5  # each 5 ounce candle requires 0.5 ounces of wax
    result = num_candles
    return result

print(solution())