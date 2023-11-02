def solution():
    """Haleigh decides that instead of throwing away old candles, she can use the last bit of wax combined together to make new candles. Each candle has 10% of it's original wax left. How many 5 ounce candles can she make if she has five 20 oz candles, 5 five ounce candles, and twenty-five one ounce candles?"""
    total_wax = 0
    for i in range(5):
        total_wax += 0.1 * 20
    for i in range(5):
        total_wax += 0.1 * 5
    for i in range(25):
        total_wax += 0.1 * 1

    num_candles = total_wax // 5
    result = num_candles
    return result

print(solution())