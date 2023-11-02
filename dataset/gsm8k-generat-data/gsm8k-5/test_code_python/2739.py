def solution():
    legacy_bars = 5  # Legacy has 5 bars of gold
    aleena_bars = legacy_bars - 2  # Aleena has 2 bars fewer than Legacy

    # Calculate the total number of bars of gold the three have
    total_bars = legacy_bars + aleena_bars + 3  # Aleena + 3 others

    # Calculate the total value of the gold
    gold_value = total_bars * 2200  # $2200 per bar of gold

    result = gold_value
    return result

print(solution())