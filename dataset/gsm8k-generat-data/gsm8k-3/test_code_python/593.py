def solution():
    """A big snowstorm caused a large amount of snow to fall onto Grandpa's farm, and the wind caused the snow to pile up into a drift.  But on the second day, it warmed up enough that half of the snowdrift melted.  The third day, it snowed again, adding another 6 inches of snow onto the snowdrift.  On the fourth day, another 18 inches of snow fell onto the snowdrift.  If the snowdrift was 34 inches deep at the end of the fourth day, how deep in inches was the drift at the end of the first day?"""
    # Define the initial depth of the snowdrift
    initial_depth = 0

    # Calculate the depth of the snowdrift at the end of each day
    day_1_depth = initial_depth
    day_2_depth = day_1_depth - (day_1_depth / 2)
    day_3_depth = day_2_depth + 6
    day_4_depth = day_3_depth + 18

    # Calculate the depth of the snowdrift at the end of the first day
    final_depth = 34
    first_day_depth = (final_depth - 18 - 6) * 2

    # Display the depth of the snowdrift at the end of the first day
    result = first_day_depth
    return result

print(solution())