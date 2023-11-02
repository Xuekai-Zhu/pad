def solution():
    snowdrift_depth = 34
    added_snow_day3 = 6
    added_snow_day4 = 18

    # Calculate the depth of the snowdrift after the third day
    melted_snow = snowdrift_depth / 2
    snowdrift_depth_day3 = melted_snow + added_snow_day3

    # Calculate the depth of the snowdrift after the second day
    original_snow_depth = snowdrift_depth_day3 - added_snow_day4

    result = original_snow_depth
    return result

print(solution())