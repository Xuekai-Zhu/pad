def solution():
    """Sam bought a heavy safe with a combination lock. There were four rows with twenty gold bars per row arranged in the safe. If each gold bar is worth $20000, calculate the total worth of the gold bars in the safe."""
    rows = 4
    bars_per_row = 20
    value_per_bar = 20000
    total_bars = rows * bars_per_row
    total_worth = total_bars * value_per_bar
    result = total_worth
    return result

print(solution())