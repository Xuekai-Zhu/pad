def solution():
    total_bars = 18  # James has 18 chocolate bars to sell
    sold_last_week = 5  # James sold 5 chocolate bars last week
    sold_this_week = 7  # James sold 7 chocolate bars this week

    # Calculate the total number of bars sold
    total_sold = sold_last_week + sold_this_week

    # Calculate the number of bars James still needs to sell
    remaining_bars = total_bars - total_sold
    result = remaining_bars
    return result

print(solution())