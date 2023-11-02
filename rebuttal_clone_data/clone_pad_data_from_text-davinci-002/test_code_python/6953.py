def solution():
    total_candles = 5 + 5 + 25
    total_ounces = 5 * 20 + 5 * 5 + 25
    ounces_left = total_ounces * 0.1
    new_candles = ounces_left / 5
    result = new_candles
    return result

print(solution())