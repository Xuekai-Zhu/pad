def solution():
    """Magdalena has an apple tree on their farm, producing very few apples each year for a while now. However, this year, the apple tree yield was excellent, and it grew 200 apples. Magdalena picked 1/5 of the fruits on the first day, twice that number on the second day, and 20 more apples than he picked on the first day on the third day. Calculate the total number of apples remaining in the tree."""
    total_apples = 200
    first_day_picked = total_apples / 5
    second_day_picked = first_day_picked * 2
    third_day_picked = first_day_picked + 20
    remaining_apples = total_apples - first_day_picked - second_day_picked - third_day_picked
    result = remaining_apples
    return result

print(solution())