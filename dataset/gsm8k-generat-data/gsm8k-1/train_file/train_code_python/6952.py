def solution():
    """Haleigh decides that instead of throwing away old candles, she can use the last bit of wax combined together to make new candles. Each candle has 10% of it's original wax left. How many 5 ounce candles can she make if she has five 20 oz candles, 5 five ounce candles, and twenty-five one ounce candles?"""
    total_wax = (5*20*0.1) + (5*5*0.1) + (25*1*0.1)
    num_new_candles = total_wax / 5
    result = num_new_candles
    return result

print(solution())