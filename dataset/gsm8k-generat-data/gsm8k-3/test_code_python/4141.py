def solution():
    """James has 18 chocolate bars to sell for the swim team. He sold 5 last week and 7 this week. How many more chocolate bars does he need to sell?"""
    # Define the number of chocolate bars James has and the number he sold so far
    total_bars = 18
    sold_bars = 5 + 7

    # Calculate the remaining number of chocolate bars James needs to sell
    remaining_bars = total_bars - sold_bars

    # Display the number of remaining chocolate bars
    result = remaining_bars
    return result

print(solution())