def solution():
    """Legacy has 5 bars of gold she received from her father. Her friend Aleena has 2 bars fewer than she has. If a bar of gold is worth $2200, calculate the total value of gold the three have together."""
    legacy_bars = 5
    aleena_bars = legacy_bars - 2
    total_bars = legacy_bars + aleena_bars
    value_per_bar = 2200
    total_value = total_bars * value_per_bar
    result = total_value
    return result

print(solution())