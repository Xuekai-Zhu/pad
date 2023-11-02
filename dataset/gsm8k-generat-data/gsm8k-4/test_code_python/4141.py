def solution():
    """James has 18 chocolate bars to sell for the swim team. He sold 5 last week and 7 this week. How many more chocolate bars does he need to sell?"""
    # Define the total number of chocolate bars and the number of bars sold
    total_bars = 18
    bars_sold = 5 + 7

    # Calculate the remaining number of bars to sell
    remaining_bars = total_bars - bars_sold

    # Return the result
    result = remaining_bars
    return result

print(solution())