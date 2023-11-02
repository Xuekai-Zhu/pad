def solution():
    """Sam bought a heavy safe with a combination lock. There were four rows with twenty gold bars per row arranged in the safe. If each gold bar is worth $20000, calculate the total worth of the gold bars in the safe."""
    # Define the number of rows and the number of gold bars per row
    NUM_ROWS = 4
    NUM_GOLD_BARS_PER_ROW = 20

    # Define the value of one gold bar
    GOLD_BAR_VALUE = 20000

    # Calculate the total number of gold bars
    total_gold_bars = NUM_ROWS * NUM_GOLD_BARS_PER_ROW

    # Calculate the total worth of the gold bars in the safe
    total_worth = total_gold_bars * GOLD_BAR_VALUE

    # return the result
    return total_worth

print(solution())