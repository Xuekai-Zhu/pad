def solution():
    total_bars = 18
    sold_last_week = 5
    sold_this_week = 7

    # Calculate the total number of bars sold so far
    total_sold = sold_last_week + sold_this_week

    # Calculate the number of bars James still needs to sell
    remaining_bars = total_bars - total_sold
    result = remaining_bars
    return result

print(solution())