def solution():
    legacy_bars = 5
    aleena_bars = legacy_bars - 2
    total_bars = legacy_bars + aleena_bars + 1  # adding 1 because it is not specified how many bars the third person has
    bar_value = 2200
    total_value = total_bars * bar_value
    result = total_value
    return result

print(solution())