def solution():
    # Calculate the total amount of wax from the old candles
    total_wax = (5 * 20 + 5 * 5 + 25 * 1) * 0.1

    # Calculate the number of 5 ounce candles that can be made
    num_candles = total_wax / 5

    result = num_candles
    return result

print(solution())