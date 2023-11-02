def solution():
    """Hannah fills her kids' stockings with 4 candy canes, 2 beanie babies and 1 book. If she has 3 kids, how many stocking stuffers does she buy total?"""
    # Define the number of stocking stuffers per kid
    CANDY_CANES = 4
    BEANIE_BABIES = 2
    BOOKS = 1

    # Define the number of kids
    KIDS = 3

    # Calculate the total number of stocking stuffers
    total_stocking_stuffers = (CANDY_CANES + BEANIE_BABIES + BOOKS) * KIDS

    # Display the total number of stocking stuffers
    result = total_stocking_stuffers
    return result

print(solution())