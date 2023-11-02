def solution():
    """Niko has bought 9 pairs of socks that cost $2 each and plans to resell them. He wants to gain 25% profit from four of the pairs of socks and $0.2 profit each for the other 5 pairs of socks. How much will his total profit be?"""
    # Define the cost and selling price of each pair of socks
    COST_PER_PAIR = 2
    SELLING_PRICE_25_PERCENT = 2.5
    SELLING_PRICE_20_CENTS = 2.2

    # Define the number of pairs that Niko wants to gain 25% profit on
    PROFIT_25_PERCENT_PAIRS = 4

    # Calculate the total cost of all the socks
    total_cost = 9 * COST_PER_PAIR

    # Calculate the profit from the 25% pairs of socks
    profit_25_percent = PROFIT_25_PERCENT_PAIRS * (SELLING_PRICE_25_PERCENT - COST_PER_PAIR)

    # Calculate the profit from the 20 cent pairs of socks
    profit_20_cents = (9 - PROFIT_25_PERCENT_PAIRS) * 0.2

    # Calculate the total profit
    total_profit = profit_25_percent + profit_20_cents

    # Display the total profit
    result = total_profit
    return result

print(solution())