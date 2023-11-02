def solution():
    legacy_bars = 5
    aleena_bars = legacy_bars - 2
    bar_value = 2200

    # Calculate the total value of gold for Legacy
    legacy_value = legacy_bars * bar_value

    # Calculate the total value of gold for Aleena
    aleena_value = aleena_bars * bar_value

    # Calculate the total value of gold for both Legacy and Aleena
    total_value = legacy_value + aleena_value + (3 * bar_value)
    result = total_value
    return result

print(solution())