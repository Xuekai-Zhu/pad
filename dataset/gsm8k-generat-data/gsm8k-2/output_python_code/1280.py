def solution():
    """Sam bought a heavy safe with a combination lock. There were four rows with twenty gold bars per row arranged in the safe. If each gold bar is worth $20000, calculate the total worth of the gold bars in the safe."""
    gold_bars_per_row = 20
    total_rows = 4
    gold_bar_worth = 20000
    total_gold_bars = gold_bars_per_row * total_rows
    total_worth = total_gold_bars * gold_bar_worth
    result = total_worth
    return result

print(solution())