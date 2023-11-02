def solution():
    num_bars = 20
    num_days = 7
    num_bars_per_day = 1
    traded_bars = 3
    num_sisters = 2

    # Calculate the total number of bars Greg has left after setting aside one each day
    remaining_bars = num_bars - (num_days * num_bars_per_day)

    # Subtract the bars traded to Pete
    remaining_bars -= traded_bars

    # Divide the remaining bars evenly between Greg's two sisters
    bars_per_sister = remaining_bars / num_sisters
    result = bars_per_sister
    return result

print(solution())