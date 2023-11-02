def solution():
    """Charlie wants to sell beeswax candles. For every pound of beeswax, he can make 10 tapered candles. One pound of beeswax and the wicks cost $10.00 in supplies. If he sells each candle for $2.00 each, what is his net profit if he makes and sells 20 candles?"""
    candles_per_pound = 10
    supply_cost_per_pound = 10
    sale_price_per_candle = 2
    candles_made = 20
    net_profit = (candles_made * sale_price_per_candle) - (supply_cost_per_pound * (candles_made // candles_per_pound))
    result = net_profit
    return result

print(solution())