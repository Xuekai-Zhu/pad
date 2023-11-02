def solution():
    """Magdalena has an apple tree on their farm, producing very few apples each year for a while now. However, this year, the apple tree yield was excellent, and it grew 200 apples. Magdalena picked 1/5 of the fruits on the first day, twice that number on the second day, and 20 more apples than he picked on the first day on the third day. Calculate the total number of apples remaining in the tree."""
    # Define the total number of apples Magdalena picked on the first day
    day_one_pick = 200 * (1/5)

    # Define the total number of apples Magdalena picked on the second day
    day_two_pick = 2 * day_one_pick

    # Define the total number of apples Magdalena picked on the third day
    day_three_pick = day_one_pick + 20

    # Calculate the total number of apples picked
    total_pick = day_one_pick + day_two_pick + day_three_pick

    # Calculate the total number of apples remaining on the tree
    remaining_apples = 200 - total_pick

    # Display the total number of apples remaining
    result = remaining_apples
    return result

print(solution())