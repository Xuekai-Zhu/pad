def solution():
    """A big snowstorm caused a large amount of snow to fall onto Grandpa's farm, and the wind caused the snow to pile up into a drift. But on the second day, it warmed up enough that half of the snowdrift melted. The third day, it snowed again, adding another 6 inches of snow onto the snowdrift. On the fourth day, another 18 inches of snow fell onto the snowdrift. If the snowdrift was 34 inches deep at the end of the fourth day, how deep in inches was the drift at the end of the first day?"""
    snowdrift_end_day4 = 34
    snowdrift_end_day3 = snowdrift_end_day4 - 18
    snowdrift_end_day2 = snowdrift_end_day3 + 6
    snowdrift_end_day1 = snowdrift_end_day2 * 2
    result = snowdrift_end_day1
    
    return result

print(solution())