def solution():
    """Magdalena has an apple tree on their farm, producing very few apples each year for a while now. However, this year, the apple tree yield was excellent, and it grew 200 apples. Magdalena picked 1/5 of the fruits on the first day, twice that number on the second day, and 20 more apples than he picked on the first day on the third day. Calculate the total number of apples remaining in the tree."""
    # Define the total number of apples on the tree
    total_apples = 200

    # Calculate the number of apples picked on the first day
    day1_apples = total_apples * (1/5)

    # Calculate the number of apples picked on the second day
    day2_apples = day1_apples * 2

    # Calculate the number of apples picked on the third day
    day3_apples = day1_apples + 20

    # Calculate the total number of apples picked
    total_picked = day1_apples + day2_apples + day3_apples

    # Calculate the number of apples remaining on the tree
    remaining_apples = total_apples - total_picked

    # return the result
    result = remaining_apples
    return result

print(solution())