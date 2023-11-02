def solution():
    """Legacy has 5 bars of gold she received from her father. Her friend Aleena has 2 bars fewer than she has. If a bar of gold is worth $2200, calculate the total value of gold the three have together."""
    # Define the value of a single gold bar in dollars
    GOLD_BAR_VALUE = 2200

    # Calculate the total number of gold bars between Legacy and Aleena
    legacy_bars = 5
    aleena_bars = legacy_bars - 2
    total_bars = legacy_bars + aleena_bars

    # Calculate the total value of the gold bars
    total_value = total_bars * GOLD_BAR_VALUE

    # return the result
    result = total_value
    return result

print(solution())