def solution():
    
    # Define the number of tapered candles that can be made with one pound of beeswax
    tapered_candles_per_pound = 10

    # Define the cost of supplies for one pound of beeswax
    supply_cost_per_pound = 10

    # Define the number of candles that can be made with 20 candles
    candles_sold = 20

    # Calculate the total number of tapered candles that can be made with 20 candles
    total_tapered_candles = tapered_candles_per_pound * candles_sold

    # Calculate the total cost of supplies for 20 candles
    total_supply_cost = supply_cost_per_pound * candles_sold

    # Calculate the total revenue from selling 20 candles
    total_revenue = total_tapered_candles * 2

    # Calculate the net profit
    net_profit = total_revenue - total_supply_cost

print(solution())