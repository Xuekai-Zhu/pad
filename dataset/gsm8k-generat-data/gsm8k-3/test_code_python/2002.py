def solution():
    """Pete used circles, to represent how many scoops of ice cream he can consume in one sitting, and squares, to represent the number of brownies he has hidden beneath his bed.  For circles, he used 3 less than half the number of stars on the US flag, and for squares, he used six more than twice the number of stripes on the US flag.  What is the combined total number of circles and squares on Pete's flag?"""
    # Define the number of stars and stripes on the US flag
    STARS = 50
    STRIPES = 13

    # Calculate the number of circles on Pete's flag
    circles = (STARS / 2) - 3

    # Calculate the number of squares on Pete's flag
    squares = (2 * STRIPES) + 6

    # Calculate the combined total number of circles and squares on Pete's flag
    combined_total = circles + squares

    # Display the combined total number of circles and squares
    result = combined_total
    return result

print(solution())