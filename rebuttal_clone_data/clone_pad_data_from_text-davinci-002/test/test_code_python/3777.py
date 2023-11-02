def solution():
    beeswax_per_candle = 8
    coconut_oil_per_candle = 1
    total_candles = 10 - 3
    total_beeswax = total_candles * beeswax_per_candle
    total_coconut_oil = total_candles * coconut_oil_per_candle
    combined_weight = total_beeswax + total_coconut_oil
    result = combined_weight
    
    return result

print(solution())