def solution():
    # Define the number of rows and gold bars per row
    num_rows = 4
    gold_bars_per_row = 20

    # Calculate the total number of gold bars
    total_gold_bars = num_rows * gold_bars_per_row

    # Calculate the total worth of the gold bars
    gold_bar_value = 20000
    total_worth = total_gold_bars * gold_bar_value
    result = total_worth
    return result

print(solution())