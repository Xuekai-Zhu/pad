def solution():
    """A big snowstorm caused a large amount of snow to fall onto Grandpa's farm, and the wind caused the snow to pile up into a drift.
    But on the second day, it warmed up enough that half of the snowdrift melted. The third day, it snowed again, adding another 6 inches of snow onto the snowdrift.
    On the fourth day, another 18 inches of snow fell onto the snowdrift.
    If the snowdrift was 34 inches deep at the end of the fourth day, how deep in inches was the drift at the end of the first day?"""
    final_depth = 34
    third_day_depth = final_depth - 18 - 6
    second_day_depth = third_day_depth / 2
    first_day_depth = second_day_depth + 18 + 6
    result = first_day_depth
    return result

print(solution())