def solution():
    num_rows = 4
    num_bars_per_row = 20
    bar_value = 20000

    # Calculate the total number of gold bars in the safe
    total_bars = num_rows * num_bars_per_row

    # Calculate the total worth of all gold bars in the safe
    total_worth = total_bars * bar_value
    result = total_worth
    return result

print(solution())