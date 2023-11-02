def solution():
    # Define the initial number of granola bars
    num_bars = 20

    # Set aside one for each day of the week
    num_bars -= 7

    # Trade three for a soda
    num_bars -= 3

    # Divide the remaining bars evenly between two sisters
    num_sisters = 2
    bars_per_sister = num_bars // num_sisters

    result = bars_per_sister
    return result

print(solution())