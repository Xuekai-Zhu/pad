def solution():
    
    # Define the number of tapered candles Charlie can make
    tapered_candles = 10

    # Define the cost of supplies per pound of beeswax and the selling price per candle
    supplies_cost = 10
    selling_price_per_candle = 2

    # Calculate the total cost of making the tapered candles
    total_cost = tapered_candles * tapered_candles * supplies_cost

    # Calculate the total revenue from selling the candles
    total_revenue = 20 * selling_price_per_candle

    # Calculate the net profit
    net_profit = total_revenue - total_cost

    # return the result
    result = net_profit
    return result

print(solution())