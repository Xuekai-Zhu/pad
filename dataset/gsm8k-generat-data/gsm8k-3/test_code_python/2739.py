def solution():
    """Legacy has 5 bars of gold she received from her father. Her friend Aleena has 2 bars fewer than she has. If a bar of gold is worth $2200, calculate the total value of gold the three have together."""
    # Define the value of a single bar of gold
    BAR_VALUE = 2200

    # Define the number of bars of gold each person has
    legacy_bars = 5
    aleena_bars = legacy_bars - 2
    friend_bars = aleena_bars

    # Calculate the total value of gold the three have together
    total_value = (legacy_bars + aleena_bars + friend_bars) * BAR_VALUE

    # Display the total value
    result = total_value
    return result

print(solution())