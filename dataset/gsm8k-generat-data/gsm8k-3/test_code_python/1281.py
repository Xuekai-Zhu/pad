def solution():
    """Sam bought a heavy safe with a combination lock. There were four rows with twenty gold bars per row arranged in the safe. If each gold bar is worth $20000, calculate the total worth of the gold bars in the safe."""
    # Define the number of rows and gold bars per row
    rows = 4
    bars_per_row = 20

    # Define the value of each gold bar
    value_per_bar = 20000

    # Calculate the total worth of the gold bars in the safe
    total_worth = rows * bars_per_row * value_per_bar

    # Display the total worth
    result = total_worth
    return result

print(solution())